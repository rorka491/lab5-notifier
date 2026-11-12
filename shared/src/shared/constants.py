from enum import StrEnum


class OperationType(StrEnum):
    PURCHASE = "purchase"
    RETURN = "return"
    REDEEM = "redeem"


class OperationStatus(StrEnum):
    APPLIED = "applied"
    REJECTED = "rejected"


class RejectReason(StrEnum):
    DUPLICATE_PURCHASE = "duplicate_purchase"
    PURCHASE_NOT_FOUND = "purchase_not_found"
    CUSTOMER_MISMATCH = "customer_mismatch"
    ALREADY_RETURNED = "already_returned"
    LIMIT_EXCEEDED = "limit_exceeded"
    INSUFFICIENT_BALANCE = "insufficient_balance"



class Exchange(StrEnum):
    LOYALTY_COMMANDS = "loyalty.commands"
    LOYALTY_EVENTS = "loyalty.events"


class Queue(StrEnum):
    OPERATIONS = "operations"
    NOTIFIER_EVENTS = "notifier_events"
    ANALYTICS_EVENTS = "analytics_events"
    

class RoutingKey(StrEnum):
    OPERATION = "operation"
    