"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _OperationType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _OperationTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _OperationType.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    EXPENSE: _OperationType.ValueType  # 0
    INCOME: _OperationType.ValueType  # 1

class OperationType(_OperationType, metaclass=_OperationTypeEnumTypeWrapper): ...

EXPENSE: OperationType.ValueType  # 0
INCOME: OperationType.ValueType  # 1
global___OperationType = OperationType

@typing.final
class Error(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Code:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _CodeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            Error._Code.ValueType
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ACCOUNT_ALREADY_EXIST: Error._Code.ValueType  # 0
        ACCOUNT_NOT_FOUND: Error._Code.ValueType  # 1

    class Code(_Code, metaclass=_CodeEnumTypeWrapper): ...
    ACCOUNT_ALREADY_EXIST: Error.Code.ValueType  # 0
    ACCOUNT_NOT_FOUND: Error.Code.ValueType  # 1

    CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    code: global___Error.Code.ValueType
    message: builtins.str
    def __init__(
        self,
        *,
        code: global___Error.Code.ValueType = ...,
        message: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["code", b"code", "message", b"message"]
    ) -> None: ...

global___Error = Error

@typing.final
class Balance(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXPENSES_FIELD_NUMBER: builtins.int
    INCOMES_FIELD_NUMBER: builtins.int
    expenses: builtins.str
    incomes: builtins.str
    def __init__(
        self,
        *,
        expenses: builtins.str = ...,
        incomes: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["expenses", b"expenses", "incomes", b"incomes"]
    ) -> None: ...

global___Balance = Balance

@typing.final
class Account(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            Account._Status.ValueType
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ACTIVE: Account._Status.ValueType  # 0
        ARCHIVE: Account._Status.ValueType  # 1

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    ACTIVE: Account.Status.ValueType  # 0
    ARCHIVE: Account.Status.ValueType  # 1

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    BALANCE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    status: global___Account.Status.ValueType
    @property
    def balance(self) -> global___Balance: ...
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        balance: global___Balance | None = ...,
        status: global___Account.Status.ValueType = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal["balance", b"balance", "created_at", b"created_at"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "balance",
            b"balance",
            "created_at",
            b"created_at",
            "id",
            b"id",
            "name",
            b"name",
            "status",
            b"status",
        ],
    ) -> None: ...

global___Account = Account

@typing.final
class Tag(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    id: builtins.str
    value: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["id", b"id", "value", b"value"]
    ) -> None: ...

global___Tag = Tag

@typing.final
class Operation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    OPERATION_TYPE_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    amount: builtins.str
    description: builtins.str
    operation_type: global___OperationType.ValueType
    account_id: builtins.str
    @property
    def tags(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.str
    ]: ...
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        amount: builtins.str = ...,
        description: builtins.str = ...,
        operation_type: global___OperationType.ValueType = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
        account_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing.Literal["created_at", b"created_at"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "account_id",
            b"account_id",
            "amount",
            b"amount",
            "created_at",
            b"created_at",
            "description",
            b"description",
            "id",
            b"id",
            "operation_type",
            b"operation_type",
            "tags",
            b"tags",
        ],
    ) -> None: ...

global___Operation = Operation

@typing.final
class AccountResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def account(self) -> global___Account: ...
    def __init__(
        self,
        *,
        account: global___Account | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing.Literal["account", b"account"]
    ) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["account", b"account"]) -> None: ...

global___AccountResponse = AccountResponse

@typing.final
class TagResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TAG_FIELD_NUMBER: builtins.int
    @property
    def tag(self) -> global___Tag: ...
    def __init__(
        self,
        *,
        tag: global___Tag | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["tag", b"tag"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["tag", b"tag"]) -> None: ...

global___TagResponse = TagResponse

@typing.final
class OperationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATION_FIELD_NUMBER: builtins.int
    @property
    def operation(self) -> global___Operation: ...
    def __init__(
        self,
        *,
        operation: global___Operation | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing.Literal["operation", b"operation"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing.Literal["operation", b"operation"]
    ) -> None: ...

global___OperationResponse = OperationResponse

@typing.final
class GetOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    account_id: builtins.str
    def __init__(
        self,
        *,
        account_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["account_id", b"account_id"]
    ) -> None: ...

global___GetOperationsRequest = GetOperationsRequest

@typing.final
class CreateAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name"]) -> None: ...

global___CreateAccountRequest = CreateAccountRequest

@typing.final
class RenameAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["id", b"id", "name", b"name"]
    ) -> None: ...

global___RenameAccountRequest = RenameAccountRequest

@typing.final
class RemoveAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___RemoveAccountRequest = RemoveAccountRequest

@typing.final
class AddOperationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AMOUNT_FIELD_NUMBER: builtins.int
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    OPERATION_TYPE_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    amount: builtins.str
    account_id: builtins.str
    description: builtins.str
    operation_type: global___OperationType.ValueType
    created_at: builtins.str
    @property
    def tags(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.str
    ]: ...
    def __init__(
        self,
        *,
        amount: builtins.str = ...,
        account_id: builtins.str = ...,
        description: builtins.str | None = ...,
        operation_type: global___OperationType.ValueType | None = ...,
        created_at: builtins.str | None = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "_created_at",
            b"_created_at",
            "_description",
            b"_description",
            "_operation_type",
            b"_operation_type",
            "created_at",
            b"created_at",
            "description",
            b"description",
            "operation_type",
            b"operation_type",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "_created_at",
            b"_created_at",
            "_description",
            b"_description",
            "_operation_type",
            b"_operation_type",
            "account_id",
            b"account_id",
            "amount",
            b"amount",
            "created_at",
            b"created_at",
            "description",
            b"description",
            "operation_type",
            b"operation_type",
            "tags",
            b"tags",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing.Literal["_created_at", b"_created_at"]
    ) -> typing.Literal["created_at"] | None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing.Literal["_description", b"_description"]
    ) -> typing.Literal["description"] | None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing.Literal["_operation_type", b"_operation_type"]
    ) -> typing.Literal["operation_type"] | None: ...

global___AddOperationRequest = AddOperationRequest

@typing.final
class RemoveOperationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___RemoveOperationRequest = RemoveOperationRequest

@typing.final
class GetLatestOperationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    account_id: builtins.str
    def __init__(
        self,
        *,
        account_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["account_id", b"account_id"]
    ) -> None: ...

global___GetLatestOperationRequest = GetLatestOperationRequest
