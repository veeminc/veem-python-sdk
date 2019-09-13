from attrdict import AttrDict

AccountType = AttrDict(dict(
    BUSINESS='Business',
    INCOMPLETE='Incomplete',
    PERSONAL='Personal'
))

ApprovalStatus = AttrDict(dict(
    APPROVED='Approved',
    PENDING='Pending',
    IGNORED='Ignored'
))

AttachmentType = AttrDict(dict(
    EXTERNAL_INVOICE='ExternalInvoice',
    PROOF_OF_PAYMENT='ProofOfPayment'
))

BatchItemType = AttrDict(dict(
    CONTACT='CONTACT',
    PAYMENT='PAYMENT'
))

BatchStatus = AttrDict(dict(
    FAILED='Failed',
    IN_PROGRESS='InProgress',
    COMPLETED='Completed'
))

Direction = AttrDict(dict(
    INBOUND='Inbound',
    OUTBOUND='Outbound'
))

InvoiceStatus = AttrDict(dict(
    DRAFTED='Drafted',
    SENT="Sent",
    CANCELLED="Cancelled",
    CLOSED="Closed",
    CLAIMED="Claimed",
    PAID="MarkAsPaid",
    REJECTED="Rejected"
))

PaymentSortField = AttrDict(dict(
    TIME_UPDATE='timeUpdated'
))

PaymentStatus = AttrDict(dict(
    DRAFTED="Drafted",
    SCHEDULED="Scheduled",
    PENDING_APPROVAL="PendingApproval",
    SENT="Sent",
    CLAIMED="Claimed",
    PENDING_AUTH="PendingAuth",
    AUTHORIZED="Authorized",
    IN_PROGRESS="InProgress",
    COMPLETE="Complete",
    CANCELLED="Cancelled",
    CLOSED="Closed",
    REVERSED="Reversed"
))

Scope = AttrDict(dict(
    All='all'
))

SortOrder = AttrDict(dict(
    ASC='asc',
    DESC='desc'
))

CLIENT_CREDENTIALS_GRANT_TYPE = "client_credentials"
AUTHORIZATION_CODE_GRANT_TYPE = "authorization_code"
REFRESH_TOKEN_GRANT_TYPE = "refresh_token"

FILE_DOWNLOAD_CHUNK_SIZE = 1024
