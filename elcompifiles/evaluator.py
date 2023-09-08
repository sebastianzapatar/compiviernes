from typing import(
    cast,
    List,
    Optional,
    Type
)
import elcompifiles.ast as ast

from elcompifiles.objects import(
    Boolean,
    Integer,
    Null,
    Object,
    ObjectType
)
TRUE=Boolean(True)
FALSE=Boolean(False)
NULL=Null()
def _evaluate_bang_operator_expression(right:Object)->Object:
    if right is TRUE:
        return FALSE
    elif right is FALSE:
        return TRUE
    elif right is NULL:
        return TRUE
    else:
        return FALSE
    
def _to_boolean_object(value:bool)->Boolean:
    return TRUE if value else FALSE

def _evaluate_minus_operator_expression(right:Object)->Object:
    if type(right)!=Integer:
        return NULL
    right=cast(Integer,right)
    return Integer(-right.value)

def _evaluate_prefix_expression(operator:str,right:Object)->Object:
    if operator=='!':
        return _evaluate_bang_operator_expression(right)
    elif operator=='-':
        return _evaluate_minus_operator_expression(right)
    else:
        return NULL
    
def __evaluate_integer_infix_expression(operator:str,
                                        left:Object,
                                        right:Object)->Optional[Object]:
    left_value:int=cast(Integer,left).value
    right_value:int=cast(Integer,right).value
    if operator=='+':
        return Integer(left_value+right_value)
    elif operator=='-':
        return Integer(left_value-right_value)
    elif operator=='*':
        return Integer(left_value*right_value)
    elif operator=='/':
        return Integer(left_value//right_value)
    elif operator=='<':
        return _to_boolean_object(left_value<right_value)
    elif operator=='<=':
        return _to_boolean_object(left_value<=right_value)
    elif operator=='>':
        return _to_boolean_object(left_value>right_value)
    elif operator=='>=':
        return _to_boolean_object(left_value>=right_value)
    elif operator=='==':
        return _to_boolean_object(left_value==right_value)
    elif operator=='!=':
        return _to_boolean_object(left_value!=right_value)
    return NULL
def _evaluate_infix_expression(operator:str,
                               left:Object,
                               right:Object)->Object:
    if left.type()==ObjectType.INTEGER\
    and right.type()==ObjectType.INTEGER:
        return __evaluate_integer_infix_expression(operator,left,right)
    elif operator=='==':
        return _to_boolean_object(left is right)
    elif operator =='!=':
        return _to_boolean_object(left is not right)
    return NULL

def evaluate(node: ast.ASTNode)->Optional[Object]:
    node_type:Type=type(node)
    if node_type==ast.Program:
        node=cast(ast.Program,node)
        return _evaluate_statements(node.statements)
    elif node_type==ast.ExpressionStatement:
        node=cast(ast.ExpressionStatement,node)
        assert node.expression is not None
        return evaluate(node.expression)
    elif node_type==ast.Integer:
        node=cast(ast.Integer,node)
        assert node.value is not None
        return Integer(node.value)
    elif node_type==ast.Boolean:
        node=cast(ast.Boolean,node)
        assert node.value is not None
        return _to_boolean_object(node.value)
    elif node_type==ast.Prefix:
        node=cast(ast.Prefix,node)
        assert node.right is not None
        right=evaluate(node.right)

        assert right is not None
        return _evaluate_prefix_expression(node.operator,right)
    elif node_type==ast.Infix:
        node=cast(ast.Infix,node)
        assert node.left is not None and node.right is not None
        left=evaluate(node.left)
        right=evaluate(node.right)
        
        assert right is not None and left is not None

        return _evaluate_infix_expression(node.operator,left,right)
    
    return None
def _evaluate_statements(statements:List[ast.Statement])->Optional[Object]:
    result:Optional[Object]=None
    for statement in statements:
        result=evaluate(statement)

    return result
