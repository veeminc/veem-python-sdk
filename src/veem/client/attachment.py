
import os
import shutil
import tempfile

from veem.constants import FILE_DOWNLOAD_CHUNK_SIZE
from veem.client.responses.attachment import AttachmentResponse

from veem.client.base import Base
from veem.utils.rest import VeemRestApi
from veem.utils import file_access_check, extract_file_content_type

from veem.models.attachment import Attachment
from veem.exceptions import VeemSdkException

class AttachmentClient(Base):

    def __init__(self, config, **kwargs):

        self.config = config
        self.context = config.context
        self.client = VeemRestApi(self.config.url,
                                  self.context.session,
                                  dict(upload=('post', ''),
                                       download=('get', '')))

    def upload(self, attachment, description):
        """
            Upload an attachment to Veem. The attachment can be referenced from
            other entities, like Payment and Invoice.

            @param attachment: An Attachment with a valid file path to a
                               readable file
            @param description: Attachment description
            @return A new Attachment with name and referenceId set
            @throws VeemException If the provided Attachment path is invalid, or
                                  if uploading fails.
        """
        attachment = Attachment(**attachment) if isinstance(
                                attachment, dict) else attachment
        file_access_check(attachment.path, raise_exception=True)
        content_type = extract_file_content_type(attachment.path)
        request_files = dict(file=(os.path.basename(attachment.path),
                                   open(attachment.path, 'rb'),
                                   content_type))
        return self._response_handler(
                        AttachmentResponse,
                        self.client.upload(access_token=self.context.token,
                                        api_route='attachments',
                                        description=description,
                                        request_files=request_files)
                            )

    def download(self, request,
                 targetDirectory=None,
                 chunk_size=FILE_DOWNLOAD_CHUNK_SIZE):
        """
            Download an attachment from Veem.

            @param attachment: An Attachment with a valid name and referenceId
            @param targetDirectory: The directory where the downloaded file will
                                    be stored
            @param chunk_size: The data chunk size to write each iteration
            @return target file path to the downloaded attachment
            @throws VeemException If the provided targetDirectory is invalid, or
                                  if downloading fails.
        """
        with self.client.download(access_token=self.context.token,
                                  api_route='attachments',
                                  request_stream=True,
                                  request_params=request.json) as stream:
            stream.raise_for_status()
            kwargs = dict(delete=False)
            # if target directory is provided, calculate path and check for
            # write access
            if targetDirectory:
                if not os.path.isdir(targetDirectory):
                    if not os.path.isfile(targetDirectory):
                        raise VeemSdkException("Unable to access directory")
                    targetDirectory = os.path.abspath(targetDirectory)

                if not os.access(targetDirectory, os.W_OK):
                    raise VeemSdkException("Target directory is not writable")

                kwargs['dir'] = targetDirectory
            # generate a temporay file, save the download content and return the
            # full path
            with tempfile.NamedTemporaryFile(**kwargs) as fp:
                for chunk in stream.iter_content(chunk_size=chunk_size):
                    if chunk:
                        fp.write(chunk)
                return fp.name
