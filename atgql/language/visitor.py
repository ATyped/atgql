from __future__ import annotations

from atgql.language.ast import (
    ASTNode,
    NameNode,
    DocumentNode,
    OperationDefinitionNode,
    VariableDefinitionNode,
    VariableNode,
    SelectionSetNode,
    FieldNode,
    ArgumentNode,
    FragmentSpreadNode,
    InlineFragmentNode,
    FragmentDefinitionNode,
    IntValueNode,
    FloatValueNode,
    StringValueNode,
    BooleanValueNode,
    NullValueNode,
    EnumValueNode,
    ListValueNode,
    ObjectValueNode,
    ObjectFieldNode,
    DirectiveNode,
    NamedTypeNode,
    ListTypeNode,
    NonNullTypeNode,
    SchemaDefinitionNode,
    OperationTypeDefinitionNode,
    ScalarTypeDefinitionNode,
    ObjectTypeDefinitionNode,
    FieldDefinitionNode,
    InputValueDefinitionNode,
    InterfaceTypeDefinitionNode,
    UnionTypeDefinitionNode,
    EnumTypeDefinitionNode,
    EnumValueDefinitionNode,
    InputObjectTypeDefinitionNode,
    DirectiveDefinitionNode,
    SchemaExtensionNode,
    ScalarTypeExtensionNode,
    ObjectTypeExtensionNode,
    InterfaceTypeExtensionNode,
    UnionTypeExtensionNode,
    EnumTypeExtensionNode,
    InputObjectTypeExtensionNode,
)
from typing import Any, Callable, Optional, Protocol, TypeVar, Union
from collections.abc import Sequence

# ASTVisitor should be defined here according to graphql-js,
# but confined by Python's syntax, ASTNode cannot refer the types defined below,
# so their definition go down to the bottom of this file.


# Python doesn't have the syntax corresponding to the TypeScript's `keyof`,
# so these types can only be manually coded.
# In order to test that there is no missing type, a test has been coded.


class _NameVisitor(Protocol):
    name: ASTVisitFn[NameNode] | EnterLeaveVisitor[NameNode]


class _DocumentVisitor(Protocol):
    document: ASTVisitFn[DocumentNode] | EnterLeaveVisitor[DocumentNode]


class _OperationDefinitionVisitor(Protocol):
    operation_definition: ASTVisitFn[OperationDefinitionNode] | EnterLeaveVisitor[
        OperationDefinitionNode
    ]


class _VariableDefinitionVisitor(Protocol):
    variable_definition: ASTVisitFn[VariableDefinitionNode] | EnterLeaveVisitor[
        VariableDefinitionNode
    ]


class _VariableVisitor(Protocol):
    variable: ASTVisitFn[VariableNode] | EnterLeaveVisitor[VariableNode]


class _SelectionSetVisitor(Protocol):
    selection_set: ASTVisitFn[SelectionSetNode] | EnterLeaveVisitor[SelectionSetNode]


class _FieldVisitor(Protocol):
    field: ASTVisitFn[FieldNode] | EnterLeaveVisitor[FieldNode]


class _ArgumentVisitor(Protocol):
    argument: ASTVisitFn[ArgumentNode] | EnterLeaveVisitor[ArgumentNode]


class _FragmentSpreadVisitor(Protocol):
    fragment_spread: ASTVisitFn[FragmentSpreadNode] | EnterLeaveVisitor[FragmentSpreadNode]


class _InlineFragmentVisitor(Protocol):
    inline_fragment: ASTVisitFn[InlineFragmentNode] | EnterLeaveVisitor[InlineFragmentNode]


class _FragmentDefinitionVisitor(Protocol):
    fragment_definition: ASTVisitFn[FragmentDefinitionNode] | EnterLeaveVisitor[
        FragmentDefinitionNode
    ]


class _IntValueVisitor(Protocol):
    int_value: ASTVisitFn[IntValueNode] | EnterLeaveVisitor[IntValueNode]


class _FloatValueVisitor(Protocol):
    float_value: ASTVisitFn[FloatValueNode] | EnterLeaveVisitor[FloatValueNode]


class _StringValueVisitor(Protocol):
    string_value: ASTVisitFn[StringValueNode] | EnterLeaveVisitor[StringValueNode]


class _BooleanValueVisitor(Protocol):
    boolean_value: ASTVisitFn[BooleanValueNode] | EnterLeaveVisitor[BooleanValueNode]


class _NullValueVisitor(Protocol):
    null_value: ASTVisitFn[NullValueNode] | EnterLeaveVisitor[NullValueNode]


class _EnumValueVisitor(Protocol):
    enum_value: ASTVisitFn[EnumValueNode] | EnterLeaveVisitor[EnumValueNode]


class _ListValueVisitor(Protocol):
    list_value: ASTVisitFn[ListValueNode] | EnterLeaveVisitor[ListValueNode]


class _ObjectValueVisitor(Protocol):
    object_value: ASTVisitFn[ObjectValueNode] | EnterLeaveVisitor[ObjectValueNode]


class _ObjectFieldVisitor(Protocol):
    object_field: ASTVisitFn[ObjectFieldNode] | EnterLeaveVisitor[ObjectFieldNode]


class _DirectiveVisitor(Protocol):
    directive: ASTVisitFn[DirectiveNode] | EnterLeaveVisitor[DirectiveNode]


class _NamedTypeVisitor(Protocol):
    named_type: ASTVisitFn[NamedTypeNode] | EnterLeaveVisitor[NamedTypeNode]


class _ListTypeVisitor(Protocol):
    list_type: ASTVisitFn[ListTypeNode] | EnterLeaveVisitor[ListTypeNode]


class _NonNullTypeVisitor(Protocol):
    non_null_type: ASTVisitFn[NonNullTypeNode] | EnterLeaveVisitor[NonNullTypeNode]


class _SchemaDefinitionVisitor(Protocol):
    schema_definition: ASTVisitFn[SchemaDefinitionNode] | EnterLeaveVisitor[SchemaDefinitionNode]


class _OperationTypeDefinitionVisitor(Protocol):
    operation_type_definition: ASTVisitFn[OperationTypeDefinitionNode] | EnterLeaveVisitor[
        OperationTypeDefinitionNode
    ]


class _ScalarTypeDefinitionVisitor(Protocol):
    scalar_type_definition: ASTVisitFn[ScalarTypeDefinitionNode] | EnterLeaveVisitor[
        ScalarTypeDefinitionNode
    ]


class _ObjectTypeDefinitionVisitor(Protocol):
    object_type_definition: ASTVisitFn[ObjectTypeDefinitionNode] | EnterLeaveVisitor[
        ObjectTypeDefinitionNode
    ]


class _FieldDefinitionVisitor(Protocol):
    field_definition: ASTVisitFn[FieldDefinitionNode] | EnterLeaveVisitor[FieldDefinitionNode]


class _InputValueDefinitionVisitor(Protocol):
    input_value_definition: ASTVisitFn[InputValueDefinitionNode] | EnterLeaveVisitor[
        InputValueDefinitionNode
    ]


class _InterfaceTypeDefinitionVisitor(Protocol):
    interface_type_definition: ASTVisitFn[InterfaceTypeDefinitionNode] | EnterLeaveVisitor[
        InterfaceTypeDefinitionNode
    ]


class _UnionTypeDefinitionVisitor(Protocol):
    union_type_definition: ASTVisitFn[UnionTypeDefinitionNode] | EnterLeaveVisitor[
        UnionTypeDefinitionNode
    ]


class _EnumTypeDefinitionVisitor(Protocol):
    enum_type_definition: ASTVisitFn[EnumTypeDefinitionNode] | EnterLeaveVisitor[
        EnumTypeDefinitionNode
    ]


class _EnumValueDefinitionVisitor(Protocol):
    enum_value_definition: ASTVisitFn[EnumValueDefinitionNode] | EnterLeaveVisitor[
        EnumValueDefinitionNode
    ]


class _InputObjectTypeDefinitionVisitor(Protocol):
    input_object_type_definition: ASTVisitFn[InputObjectTypeDefinitionNode] | EnterLeaveVisitor[
        InputObjectTypeDefinitionNode
    ]


class _DirectiveDefinitionVisitor(Protocol):
    directive_definition: ASTVisitFn[DirectiveDefinitionNode] | EnterLeaveVisitor[
        DirectiveDefinitionNode
    ]


class _SchemaExtensionVisitor(Protocol):
    schema_extension: ASTVisitFn[SchemaExtensionNode] | EnterLeaveVisitor[SchemaExtensionNode]


class _ScalarTypeExtensionVisitor(Protocol):
    scalar_type_extension: ASTVisitFn[ScalarTypeExtensionNode] | EnterLeaveVisitor[
        ScalarTypeExtensionNode
    ]


class _ObjectTypeExtensionVisitor(Protocol):
    object_type_extension: ASTVisitFn[ObjectTypeExtensionNode] | EnterLeaveVisitor[
        ObjectTypeExtensionNode
    ]


class _InterfaceTypeExtensionVisitor(Protocol):
    interface_type_extension: ASTVisitFn[InterfaceTypeExtensionNode] | EnterLeaveVisitor[
        InterfaceTypeExtensionNode
    ]


class _UnionTypeExtensionVisitor(Protocol):
    union_type_extension: ASTVisitFn[UnionTypeExtensionNode] | EnterLeaveVisitor[
        UnionTypeExtensionNode
    ]


class _EnumTypeExtensionVisitor(Protocol):
    enum_type_extension: ASTVisitFn[EnumTypeExtensionNode] | EnterLeaveVisitor[
        EnumTypeExtensionNode
    ]


class _InputObjectTypeExtensionVisitor(Protocol):
    input_object_type_extension: ASTVisitFn[InputObjectTypeExtensionNode] | EnterLeaveVisitor[
        InputObjectTypeExtensionNode
    ]


KindVisitor = Union[
    _NameVisitor,
    _DocumentVisitor,
    _OperationDefinitionVisitor,
    _VariableDefinitionVisitor,
    _VariableVisitor,
    _SelectionSetVisitor,
    _FieldVisitor,
    _ArgumentVisitor,
    _FragmentSpreadVisitor,
    _InlineFragmentVisitor,
    _FragmentDefinitionVisitor,
    _IntValueVisitor,
    _FloatValueVisitor,
    _StringValueVisitor,
    _BooleanValueVisitor,
    _NullValueVisitor,
    _EnumValueVisitor,
    _ListValueVisitor,
    _ObjectValueVisitor,
    _ObjectFieldVisitor,
    _DirectiveVisitor,
    _NamedTypeVisitor,
    _ListTypeVisitor,
    _NonNullTypeVisitor,
    _SchemaDefinitionVisitor,
    _OperationTypeDefinitionVisitor,
    _ScalarTypeDefinitionVisitor,
    _ObjectTypeDefinitionVisitor,
    _FieldDefinitionVisitor,
    _InputValueDefinitionVisitor,
    _InterfaceTypeDefinitionVisitor,
    _UnionTypeDefinitionVisitor,
    _EnumTypeDefinitionVisitor,
    _EnumValueDefinitionVisitor,
    _InputObjectTypeDefinitionVisitor,
    _DirectiveDefinitionVisitor,
    _SchemaExtensionVisitor,
    _ScalarTypeExtensionVisitor,
    _ObjectTypeExtensionVisitor,
    _InterfaceTypeExtensionVisitor,
    _UnionTypeExtensionVisitor,
    _EnumTypeExtensionVisitor,
    _InputObjectTypeExtensionVisitor,
]


TVisitedNode = TypeVar('TVisitedNode', bound=ASTNode, covariant=True)


class _EnterVisitor(Protocol[TVisitedNode]):
    enter: ASTVisitFn[TVisitedNode]


class _LeaveVisitor(Protocol[TVisitedNode]):
    leave: ASTVisitFn[TVisitedNode]


EnterLeaveVisitor = Union[_EnterVisitor[TVisitedNode], _LeaveVisitor[TVisitedNode]]


# The reason why not define ASTVisitFn as Protocol, is that ASTVisitFn use TVisitedNode as argument,
# which means convariant TVisitedNode must be contravariant.

# A visitor is comprised of visit functions, which are called on each node
# during the visitor's traversal.
ASTVisitFn = Callable[
    [
        # node
        # The current node being visiting.
        TVisitedNode,
        # key
        # The index or key to this node from the parent node or Array.
        Optional[str | int],
        # parent
        # The parent immediately above this node, which may be an Array.
        Optional[ASTNode],
        # path
        # The key path to get to this node from the root node.
        Sequence[str | int],
        # ancestors
        # All nodes and Arrays visited before reaching parent of this node.
        # These correspond to array indices in `path`.
        # Note: ancestors includes arrays which contain the parent of visited node.
        Sequence[ASTNode | Sequence[ASTNode]],
    ],
    Any,
]

ASTNodeType = TypeVar('ASTNodeType', bound=ASTNode, covariant=True)
R = TypeVar('R')


class _NodeReducerWithEnter(Protocol[ASTNodeType, R]):
    enter: ASTVisitFn[ASTNodeType]
    leave: ASTReducerFn[ASTNodeType, R]


class _NodeReducerWithoutEnter(Protocol[ASTNodeType, R]):
    leave: ASTReducerFn[ASTNodeType, R]


_NodeReducer = Union[
    _NodeReducerWithEnter[ASTNodeType, R], _NodeReducerWithoutEnter[ASTNodeType, R]
]


class _NameReducer(Protocol[R]):
    name: _NodeReducer[NameNode, R]


class _DocumentReducer(Protocol[R]):
    document: _NodeReducer[DocumentNode, R]


class _OperationDefinitionReducer(Protocol[R]):
    operation_definition: _NodeReducer[OperationDefinitionNode, R]


class _VariableDefinitionReducer(Protocol[R]):
    variable_definition: _NodeReducer[VariableDefinitionNode, R]


class _VariableReducer(Protocol[R]):
    variable: _NodeReducer[VariableNode, R]


class _SelectionSetReducer(Protocol[R]):
    selection_set: _NodeReducer[SelectionSetNode, R]


class _FieldReducer(Protocol[R]):
    field: _NodeReducer[FieldNode, R]


class _ArgumentReducer(Protocol[R]):
    argument: _NodeReducer[ArgumentNode, R]


class _FragmentSpreadReducer(Protocol[R]):
    fragment_spread: _NodeReducer[FragmentSpreadNode, R]


class _InlineFragmentReducer(Protocol[R]):
    inline_fragment: _NodeReducer[InlineFragmentNode, R]


class _FragmentDefinitionReducer(Protocol[R]):
    fragment_definition: _NodeReducer[FragmentDefinitionNode, R]


class _IntValueReducer(Protocol[R]):
    int_value: _NodeReducer[IntValueNode, R]


class _FloatValueReducer(Protocol[R]):
    float_value: _NodeReducer[FloatValueNode, R]


class _StringValueReducer(Protocol[R]):
    string_value: _NodeReducer[StringValueNode, R]


class _BooleanValueReducer(Protocol[R]):
    boolean_value: _NodeReducer[BooleanValueNode, R]


class _NullValueReducer(Protocol[R]):
    null_value: _NodeReducer[NullValueNode, R]


class _EnumValueReducer(Protocol[R]):
    enum_value: _NodeReducer[EnumValueNode, R]


class _ListValueReducer(Protocol[R]):
    list_value: _NodeReducer[ListValueNode, R]


class _ObjectValueReducer(Protocol[R]):
    object_value: _NodeReducer[ObjectValueNode, R]


class _ObjectFieldReducer(Protocol[R]):
    object_field: _NodeReducer[ObjectFieldNode, R]


class _DirectiveReducer(Protocol[R]):
    directive: _NodeReducer[DirectiveNode, R]


class _NamedTypeReducer(Protocol[R]):
    named_type: _NodeReducer[NamedTypeNode, R]


class _ListTypeReducer(Protocol[R]):
    list_type: _NodeReducer[ListTypeNode, R]


class _NonNullTypeReducer(Protocol[R]):
    non_null_type: _NodeReducer[NonNullTypeNode, R]


class _SchemaDefinitionReducer(Protocol[R]):
    schema_definition: _NodeReducer[SchemaDefinitionNode, R]


class _OperationTypeDefinitionReducer(Protocol[R]):
    operation_type_definition: _NodeReducer[OperationTypeDefinitionNode, R]


class _ScalarTypeDefinitionReducer(Protocol[R]):
    scalar_type_definition: _NodeReducer[ScalarTypeDefinitionNode, R]


class _ObjectTypeDefinitionReducer(Protocol[R]):
    object_type_definition: _NodeReducer[ObjectTypeDefinitionNode, R]


class _FieldDefinitionReducer(Protocol[R]):
    field_definition: _NodeReducer[FieldDefinitionNode, R]


class _InputValueDefinitionReducer(Protocol[R]):
    input_value_definition: _NodeReducer[InputValueDefinitionNode, R]


class _InterfaceTypeDefinitionReducer(Protocol[R]):
    interface_type_definition: _NodeReducer[InterfaceTypeDefinitionNode, R]


class _UnionTypeDefinitionReducer(Protocol[R]):
    union_type_definition: _NodeReducer[UnionTypeDefinitionNode, R]


class _EnumTypeDefinitionReducer(Protocol[R]):
    enum_type_definition: _NodeReducer[EnumTypeDefinitionNode, R]


class _EnumValueDefinitionReducer(Protocol[R]):
    enum_value_definition: _NodeReducer[EnumValueDefinitionNode, R]


class _InputObjectTypeDefinitionReducer(Protocol[R]):
    input_object_type_definition: _NodeReducer[InputObjectTypeDefinitionNode, R]


class _DirectiveDefinitionReducer(Protocol[R]):
    directive_definition: _NodeReducer[DirectiveDefinitionNode, R]


class _SchemaExtensionReducer(Protocol[R]):
    schema_extension: _NodeReducer[SchemaExtensionNode, R]


class _ScalarTypeExtensionReducer(Protocol[R]):
    scalar_type_extension: _NodeReducer[ScalarTypeExtensionNode, R]


class _ObjectTypeExtensionReducer(Protocol[R]):
    object_type_extension: _NodeReducer[ObjectTypeExtensionNode, R]


class _InterfaceTypeExtensionReducer(Protocol[R]):
    interface_type_extension: _NodeReducer[InterfaceTypeExtensionNode, R]


class _UnionTypeExtensionReducer(Protocol[R]):
    union_type_extension: _NodeReducer[UnionTypeExtensionNode, R]


class _EnumTypeExtensionReducer(Protocol[R]):
    enum_type_extension: _NodeReducer[EnumTypeExtensionNode, R]


class _InputObjectTypeExtensionReducer(Protocol[R]):
    input_object_type_extension: _NodeReducer[InputObjectTypeExtensionNode, R]


ASTReducer = Union[
    _NameReducer,
    _DocumentReducer,
    _OperationDefinitionReducer,
    _VariableDefinitionReducer,
    _VariableReducer,
    _SelectionSetReducer,
    _FieldReducer,
    _ArgumentReducer,
    _FragmentSpreadReducer,
    _InlineFragmentReducer,
    _FragmentDefinitionReducer,
    _IntValueReducer,
    _FloatValueReducer,
    _StringValueReducer,
    _BooleanValueReducer,
    _NullValueReducer,
    _EnumValueReducer,
    _ListValueReducer,
    _ObjectValueReducer,
    _ObjectFieldReducer,
    _DirectiveReducer,
    _NamedTypeReducer,
    _ListTypeReducer,
    _NonNullTypeReducer,
    _SchemaDefinitionReducer,
    _OperationTypeDefinitionReducer,
    _ScalarTypeDefinitionReducer,
    _ObjectTypeDefinitionReducer,
    _FieldDefinitionReducer,
    _InputValueDefinitionReducer,
    _InterfaceTypeDefinitionReducer,
    _UnionTypeDefinitionReducer,
    _EnumTypeDefinitionReducer,
    _EnumValueDefinitionReducer,
    _InputObjectTypeDefinitionReducer,
    _DirectiveDefinitionReducer,
    _SchemaExtensionReducer,
    _ScalarTypeExtensionReducer,
    _ObjectTypeExtensionReducer,
    _InterfaceTypeExtensionReducer,
    _UnionTypeExtensionReducer,
    _EnumTypeExtensionReducer,
    _InputObjectTypeExtensionReducer,
]

TReducedNode = TypeVar('TReducedNode', bound=ASTNode, covariant=True)


ASTReducerFn = Callable[
    [
        ASTNodeType,
        Optional[str | int],
        Optional[ASTNode | Sequence[ASTNode]],
        Sequence[str | int],
        Sequence[ASTNode | Sequence[ASTNode]],
    ],
    R,
]


T = TypeVar('T')

# TODO: re-consider implementation
ReducedField = Union[Optional[T], Sequence[T], R]

# ASTVisitor should not be defined here according to graphql-js,
# but confined by Python's syntax, ASTNode can only refer the types defined above,
# so their definition settle down here.

# A visitor is provided to visit, it contains the collection of
# relevant functions to be called during the visitor's traversal.
ASTVisitor = Union[EnterLeaveVisitor[ASTNode], KindVisitor]
