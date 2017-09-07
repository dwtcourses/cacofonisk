"""
List the hangup causes of Asterisk.

These are the reasons why an Asterisk channel has ended.
Taken from: https://wiki.asterisk.org/wiki/display/AST/Hangup+Cause+Mappings
"""
AST_CAUSE_UNALLOCATED = 1
AST_CAUSE_NO_ROUTE_TRANSIT_NET = 2
AST_CAUSE_NO_ROUTE_DESTINATION = 3
AST_CAUSE_MISDIALLED_TRUNK_PREFIX = 5
AST_CAUSE_CHANNEL_UNACCEPTABLE = 6
AST_CAUSE_CALL_AWARDED_DELIVERED = 7
AST_CAUSE_PRE_EMPTED = 8
AST_CAUSE_NUMBER_PORTED_NOT_HERE = 14
AST_CAUSE_NORMAL_CLEARING = 16
AST_CAUSE_USER_BUSY = 17
AST_CAUSE_NO_USER_RESPONSE = 18
AST_CAUSE_NO_ANSWER = 19
AST_CAUSE_SUBSCRIBER_ABSENT = 20
AST_CAUSE_CALL_REJECTED = 21
AST_CAUSE_NUMBER_CHANGED = 22
AST_CAUSE_REDIRECTED_TO_NEW_DESTINATION = 23
AST_CAUSE_ANSWERED_ELSEWHERE = 26
AST_CAUSE_DESTINATION_OUT_OF_ORDER = 27
AST_CAUSE_INVALID_NUMBER_FORMAT = 28
AST_CAUSE_FACILITY_REJECTED = 29
AST_CAUSE_RESPONSE_TO_STATUS_ENQUIRY = 30
AST_CAUSE_NORMAL_UNSPECIFIED = 31
AST_CAUSE_NORMAL_CIRCUIT_CONGESTION = 34
AST_CAUSE_NETWORK_OUT_OF_ORDER = 38
AST_CAUSE_NORMAL_TEMPORARY_FAILURE = 41
AST_CAUSE_SWITCH_CONGESTION = 42
AST_CAUSE_ACCESS_INFO_DISCARDED = 43
AST_CAUSE_REQUESTED_CHAN_UNAVAIL = 44
AST_CAUSE_FACILITY_NOT_SUBSCRIBED = 50
AST_CAUSE_OUTGOING_CALL_BARRED = 52
AST_CAUSE_INCOMING_CALL_BARRED = 54
AST_CAUSE_BEARERCAPABILITY_NOTAUTH = 57
AST_CAUSE_BEARERCAPABILITY_NOTAVAIL = 58
AST_CAUSE_BEARERCAPABILITY_NOTIMPL = 65
AST_CAUSE_CHAN_NOT_IMPLEMENTED = 66
AST_CAUSE_FACILITY_NOT_IMPLEMENTED = 69
AST_CAUSE_INVALID_CALL_REFERENCE = 81
AST_CAUSE_INCOMPATIBLE_DESTINATION = 88
AST_CAUSE_INVALID_MSG_UNSPECIFIED = 95
AST_CAUSE_MANDATORY_IE_MISSING = 96
AST_CAUSE_MESSAGE_TYPE_NONEXIST = 97
AST_CAUSE_WRONG_MESSAGE = 98
AST_CAUSE_IE_NONEXIST = 99
AST_CAUSE_INVALID_IE_CONTENTS = 100
AST_CAUSE_WRONG_CALL_STATE = 101
AST_CAUSE_RECOVERY_ON_TIMER_EXPIRE = 102
AST_CAUSE_PROTOCOL_ERROR = 111
AST_CAUSE_INTERWORKING = 127
