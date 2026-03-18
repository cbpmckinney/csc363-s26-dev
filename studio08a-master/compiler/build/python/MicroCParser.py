# Generated from python/MicroC.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO



from typing import List

from MicroCCompiler.compiler.SymbolTable import SymbolTable
from MicroCCompiler.compiler.Scope import Scope
from MicroCCompiler.ast.IntLitNode import IntLitNode
from MicroCCompiler.ast.FloatLitNode import FloatLitNode
from MicroCCompiler.ast.AssignNode import AssignNode
from MicroCCompiler.ast.VarNode import VarNode
from MicroCCompiler.ast.WriteNode import WriteNode
from MicroCCompiler.ast.ReadNode import ReadNode
from MicroCCompiler.ast.ReturnNode import ReturnNode
from MicroCCompiler.ast.CondNode import CondNode
from MicroCCompiler.ast.CallNode import CallNode
from MicroCCompiler.ast.IfStatementNode import IfStatementNode
from MicroCCompiler.ast.WhileNode import WhileNode
from MicroCCompiler.ast.StatementListNode import StatementListNode
from MicroCCompiler.ast.ASTNode import ASTNode
from MicroCCompiler.ast.BinaryOpNode import BinaryOpNode
from MicroCCompiler.ast.UnaryOpNode import UnaryOpNode
from MicroCCompiler.ast.FunctionListNode import FunctionListNode
from MicroCCompiler.ast.FunctionNode import FunctionNode
from MicroCCompiler.ast.PtrDerefNode import PtrDerefNode
from MicroCCompiler.ast.AddrOfNode import AddrOfNode
from MicroCCompiler.ast.MallocNode import MallocNode
from MicroCCompiler.ast.FreeNode import FreeNode
from MicroCCompiler.ast.CastNode import CastNode
from MicroCCompiler.ast.ShiftNode import ShiftNode


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*")
        buf.write("\u01c8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3e\n\3\3\4\3\4")
        buf.write("\3\4\3\4\5\4k\n\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u0082")
        buf.write("\n\b\f\b\16\b\u0085\13\b\3\t\3\t\3\t\3\t\5\t\u008b\n\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\5\n\u0092\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\f\u00a1\n\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00b4\n\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\5\17\u00bc\n\17\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u00c7\n\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00d3\n\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u00e4\n\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u00f8\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0105\n\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u011d\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u012e\n\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u014b\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u015d\n\37\3 \3 \3 \3 \3 \3 \3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \7 \u016c\n \f \16 \u016f\13 \3!\3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u0183\n")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\5\"\u018a\n\"\3#\3#\3#\3#\3#\3#")
        buf.write("\5#\u0192\n#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\7%\u01a8\n%\f%\16%\u01ab\13%\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\7&\u01b6\n&\f&\16&\u01b9\13&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\2\6\16>")
        buf.write("HJ,\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRT\2\6\3\2\33 \4\2\6\6!!\4\2\25")
        buf.write("\25\"\"\3\2#$\2\u01c3\2V\3\2\2\2\4d\3\2\2\2\6j\3\2\2\2")
        buf.write("\bl\3\2\2\2\nn\3\2\2\2\fs\3\2\2\2\16z\3\2\2\2\20\u008a")
        buf.write("\3\2\2\2\22\u0091\3\2\2\2\24\u0093\3\2\2\2\26\u00a0\3")
        buf.write("\2\2\2\30\u00a2\3\2\2\2\32\u00b3\3\2\2\2\34\u00bb\3\2")
        buf.write("\2\2\36\u00bd\3\2\2\2 \u00c6\3\2\2\2\"\u00d2\3\2\2\2$")
        buf.write("\u00e3\3\2\2\2&\u00e5\3\2\2\2(\u00eb\3\2\2\2*\u00f7\3")
        buf.write("\2\2\2,\u00f9\3\2\2\2.\u0104\3\2\2\2\60\u011c\3\2\2\2")
        buf.write("\62\u011e\3\2\2\2\64\u012d\3\2\2\2\66\u014a\3\2\2\28\u014c")
        buf.write("\3\2\2\2:\u0150\3\2\2\2<\u015c\3\2\2\2>\u015e\3\2\2\2")
        buf.write("@\u0182\3\2\2\2B\u0189\3\2\2\2D\u0191\3\2\2\2F\u0193\3")
        buf.write("\2\2\2H\u0199\3\2\2\2J\u01ac\3\2\2\2L\u01ba\3\2\2\2N\u01bf")
        buf.write("\3\2\2\2P\u01c1\3\2\2\2R\u01c3\3\2\2\2T\u01c5\3\2\2\2")
        buf.write("VW\5\4\3\2WX\5\26\f\2XY\b\2\1\2Y\3\3\2\2\2Z[\5\n\6\2[")
        buf.write("\\\5\4\3\2\\e\3\2\2\2]^\5\f\7\2^_\5\4\3\2_e\3\2\2\2`a")
        buf.write("\5\24\13\2ab\5\4\3\2be\3\2\2\2ce\3\2\2\2dZ\3\2\2\2d]\3")
        buf.write("\2\2\2d`\3\2\2\2dc\3\2\2\2e\5\3\2\2\2fg\5\n\6\2gh\5\6")
        buf.write("\4\2hk\3\2\2\2ik\3\2\2\2jf\3\2\2\2ji\3\2\2\2k\7\3\2\2")
        buf.write("\2lm\7%\2\2m\t\3\2\2\2no\5\16\b\2op\5\b\5\2pq\7\3\2\2")
        buf.write("qr\b\6\1\2r\13\3\2\2\2st\7\4\2\2tu\5\b\5\2uv\7\5\2\2v")
        buf.write("w\7(\2\2wx\7\3\2\2xy\b\7\1\2y\r\3\2\2\2z{\b\b\1\2{|\5")
        buf.write("\20\t\2|}\b\b\1\2}\u0083\3\2\2\2~\177\f\3\2\2\177\u0080")
        buf.write("\7\6\2\2\u0080\u0082\b\b\1\2\u0081~\3\2\2\2\u0082\u0085")
        buf.write("\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084")
        buf.write("\17\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0087\7\7\2\2\u0087")
        buf.write("\u008b\b\t\1\2\u0088\u0089\7\b\2\2\u0089\u008b\b\t\1\2")
        buf.write("\u008a\u0086\3\2\2\2\u008a\u0088\3\2\2\2\u008b\21\3\2")
        buf.write("\2\2\u008c\u008d\5\16\b\2\u008d\u008e\b\n\1\2\u008e\u0092")
        buf.write("\3\2\2\2\u008f\u0090\7\t\2\2\u0090\u0092\b\n\1\2\u0091")
        buf.write("\u008c\3\2\2\2\u0091\u008f\3\2\2\2\u0092\23\3\2\2\2\u0093")
        buf.write("\u0094\5\22\n\2\u0094\u0095\5\b\5\2\u0095\u0096\7\n\2")
        buf.write("\2\u0096\u0097\5\32\16\2\u0097\u0098\7\13\2\2\u0098\u0099")
        buf.write("\7\3\2\2\u0099\u009a\b\13\1\2\u009a\25\3\2\2\2\u009b\u009c")
        buf.write("\5\30\r\2\u009c\u009d\5\26\f\2\u009d\u009e\b\f\1\2\u009e")
        buf.write("\u00a1\3\2\2\2\u009f\u00a1\b\f\1\2\u00a0\u009b\3\2\2\2")
        buf.write("\u00a0\u009f\3\2\2\2\u00a1\27\3\2\2\2\u00a2\u00a3\5\22")
        buf.write("\n\2\u00a3\u00a4\5\b\5\2\u00a4\u00a5\7\n\2\2\u00a5\u00a6")
        buf.write("\5\32\16\2\u00a6\u00a7\7\13\2\2\u00a7\u00a8\b\r\1\2\u00a8")
        buf.write("\u00a9\7\f\2\2\u00a9\u00aa\5\6\4\2\u00aa\u00ab\5 \21\2")
        buf.write("\u00ab\u00ac\7\r\2\2\u00ac\u00ad\b\r\1\2\u00ad\31\3\2")
        buf.write("\2\2\u00ae\u00af\5\36\20\2\u00af\u00b0\5\34\17\2\u00b0")
        buf.write("\u00b1\b\16\1\2\u00b1\u00b4\3\2\2\2\u00b2\u00b4\b\16\1")
        buf.write("\2\u00b3\u00ae\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\33\3")
        buf.write("\2\2\2\u00b5\u00b6\7\16\2\2\u00b6\u00b7\5\36\20\2\u00b7")
        buf.write("\u00b8\5\34\17\2\u00b8\u00b9\b\17\1\2\u00b9\u00bc\3\2")
        buf.write("\2\2\u00ba\u00bc\b\17\1\2\u00bb\u00b5\3\2\2\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bc\35\3\2\2\2\u00bd\u00be\5\16\b\2\u00be\u00bf")
        buf.write("\5\b\5\2\u00bf\u00c0\b\20\1\2\u00c0\37\3\2\2\2\u00c1\u00c2")
        buf.write("\5\"\22\2\u00c2\u00c3\5 \21\2\u00c3\u00c4\b\21\1\2\u00c4")
        buf.write("\u00c7\3\2\2\2\u00c5\u00c7\b\21\1\2\u00c6\u00c1\3\2\2")
        buf.write("\2\u00c6\u00c5\3\2\2\2\u00c7!\3\2\2\2\u00c8\u00c9\5$\23")
        buf.write("\2\u00c9\u00ca\7\3\2\2\u00ca\u00cb\b\22\1\2\u00cb\u00d3")
        buf.write("\3\2\2\2\u00cc\u00cd\5\60\31\2\u00cd\u00ce\b\22\1\2\u00ce")
        buf.write("\u00d3\3\2\2\2\u00cf\u00d0\5\62\32\2\u00d0\u00d1\b\22")
        buf.write("\1\2\u00d1\u00d3\3\2\2\2\u00d2\u00c8\3\2\2\2\u00d2\u00cc")
        buf.write("\3\2\2\2\u00d2\u00cf\3\2\2\2\u00d3#\3\2\2\2\u00d4\u00d5")
        buf.write("\5,\27\2\u00d5\u00d6\b\23\1\2\u00d6\u00e4\3\2\2\2\u00d7")
        buf.write("\u00d8\5&\24\2\u00d8\u00d9\b\23\1\2\u00d9\u00e4\3\2\2")
        buf.write("\2\u00da\u00db\5(\25\2\u00db\u00dc\b\23\1\2\u00dc\u00e4")
        buf.write("\3\2\2\2\u00dd\u00de\5*\26\2\u00de\u00df\b\23\1\2\u00df")
        buf.write("\u00e4\3\2\2\2\u00e0\u00e1\5@!\2\u00e1\u00e2\b\23\1\2")
        buf.write("\u00e2\u00e4\3\2\2\2\u00e3\u00d4\3\2\2\2\u00e3\u00d7\3")
        buf.write("\2\2\2\u00e3\u00da\3\2\2\2\u00e3\u00dd\3\2\2\2\u00e3\u00e0")
        buf.write("\3\2\2\2\u00e4%\3\2\2\2\u00e5\u00e6\7\17\2\2\u00e6\u00e7")
        buf.write("\7\n\2\2\u00e7\u00e8\5\b\5\2\u00e8\u00e9\7\13\2\2\u00e9")
        buf.write("\u00ea\b\24\1\2\u00ea\'\3\2\2\2\u00eb\u00ec\7\20\2\2\u00ec")
        buf.write("\u00ed\7\n\2\2\u00ed\u00ee\5H%\2\u00ee\u00ef\7\13\2\2")
        buf.write("\u00ef\u00f0\b\25\1\2\u00f0)\3\2\2\2\u00f1\u00f2\7\21")
        buf.write("\2\2\u00f2\u00f3\5H%\2\u00f3\u00f4\b\26\1\2\u00f4\u00f8")
        buf.write("\3\2\2\2\u00f5\u00f6\7\21\2\2\u00f6\u00f8\b\26\1\2\u00f7")
        buf.write("\u00f1\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8+\3\2\2\2\u00f9")
        buf.write("\u00fa\5.\30\2\u00fa\u00fb\7\5\2\2\u00fb\u00fc\5H%\2\u00fc")
        buf.write("\u00fd\b\27\1\2\u00fd-\3\2\2\2\u00fe\u00ff\5\64\33\2\u00ff")
        buf.write("\u0100\b\30\1\2\u0100\u0105\3\2\2\2\u0101\u0102\5> \2")
        buf.write("\u0102\u0103\b\30\1\2\u0103\u0105\3\2\2\2\u0104\u00fe")
        buf.write("\3\2\2\2\u0104\u0101\3\2\2\2\u0105/\3\2\2\2\u0106\u0107")
        buf.write("\7\22\2\2\u0107\u0108\7\n\2\2\u0108\u0109\5L\'\2\u0109")
        buf.write("\u010a\7\13\2\2\u010a\u010b\7\f\2\2\u010b\u010c\5 \21")
        buf.write("\2\u010c\u010d\7\r\2\2\u010d\u010e\b\31\1\2\u010e\u011d")
        buf.write("\3\2\2\2\u010f\u0110\7\22\2\2\u0110\u0111\7\n\2\2\u0111")
        buf.write("\u0112\5L\'\2\u0112\u0113\7\13\2\2\u0113\u0114\7\f\2\2")
        buf.write("\u0114\u0115\5 \21\2\u0115\u0116\7\r\2\2\u0116\u0117\7")
        buf.write("\23\2\2\u0117\u0118\7\f\2\2\u0118\u0119\5 \21\2\u0119")
        buf.write("\u011a\7\r\2\2\u011a\u011b\b\31\1\2\u011b\u011d\3\2\2")
        buf.write("\2\u011c\u0106\3\2\2\2\u011c\u010f\3\2\2\2\u011d\61\3")
        buf.write("\2\2\2\u011e\u011f\7\24\2\2\u011f\u0120\7\n\2\2\u0120")
        buf.write("\u0121\5L\'\2\u0121\u0122\7\13\2\2\u0122\u0123\7\f\2\2")
        buf.write("\u0123\u0124\5 \21\2\u0124\u0125\7\r\2\2\u0125\u0126\b")
        buf.write("\32\1\2\u0126\63\3\2\2\2\u0127\u0128\5\b\5\2\u0128\u0129")
        buf.write("\b\33\1\2\u0129\u012e\3\2\2\2\u012a\u012b\5:\36\2\u012b")
        buf.write("\u012c\b\33\1\2\u012c\u012e\3\2\2\2\u012d\u0127\3\2\2")
        buf.write("\2\u012d\u012a\3\2\2\2\u012e\65\3\2\2\2\u012f\u0130\5")
        buf.write("\64\33\2\u0130\u0131\b\34\1\2\u0131\u014b\3\2\2\2\u0132")
        buf.write("\u0133\5F$\2\u0133\u0134\b\34\1\2\u0134\u014b\3\2\2\2")
        buf.write("\u0135\u0136\5<\37\2\u0136\u0137\b\34\1\2\u0137\u014b")
        buf.write("\3\2\2\2\u0138\u0139\7\n\2\2\u0139\u013a\5H%\2\u013a\u013b")
        buf.write("\7\13\2\2\u013b\u013c\b\34\1\2\u013c\u014b\3\2\2\2\u013d")
        buf.write("\u013e\58\35\2\u013e\u013f\b\34\1\2\u013f\u014b\3\2\2")
        buf.write("\2\u0140\u0141\5@!\2\u0141\u0142\b\34\1\2\u0142\u014b")
        buf.write("\3\2\2\2\u0143\u0144\5> \2\u0144\u0145\b\34\1\2\u0145")
        buf.write("\u014b\3\2\2\2\u0146\u0147\7&\2\2\u0147\u014b\b\34\1\2")
        buf.write("\u0148\u0149\7\'\2\2\u0149\u014b\b\34\1\2\u014a\u012f")
        buf.write("\3\2\2\2\u014a\u0132\3\2\2\2\u014a\u0135\3\2\2\2\u014a")
        buf.write("\u0138\3\2\2\2\u014a\u013d\3\2\2\2\u014a\u0140\3\2\2\2")
        buf.write("\u014a\u0143\3\2\2\2\u014a\u0146\3\2\2\2\u014a\u0148\3")
        buf.write("\2\2\2\u014b\67\3\2\2\2\u014c\u014d\7\25\2\2\u014d\u014e")
        buf.write("\5H%\2\u014e\u014f\b\35\1\2\u014f9\3\2\2\2\u0150\u0151")
        buf.write("\7\6\2\2\u0151\u0152\5\66\34\2\u0152\u0153\b\36\1\2\u0153")
        buf.write(";\3\2\2\2\u0154\u0155\7\26\2\2\u0155\u0156\5\64\33\2\u0156")
        buf.write("\u0157\b\37\1\2\u0157\u015d\3\2\2\2\u0158\u0159\7\26\2")
        buf.write("\2\u0159\u015a\5> \2\u015a\u015b\b\37\1\2\u015b\u015d")
        buf.write("\3\2\2\2\u015c\u0154\3\2\2\2\u015c\u0158\3\2\2\2\u015d")
        buf.write("=\3\2\2\2\u015e\u015f\b \1\2\u015f\u0160\5\64\33\2\u0160")
        buf.write("\u0161\7\27\2\2\u0161\u0162\5H%\2\u0162\u0163\7\30\2\2")
        buf.write("\u0163\u0164\b \1\2\u0164\u016d\3\2\2\2\u0165\u0166\f")
        buf.write("\3\2\2\u0166\u0167\7\27\2\2\u0167\u0168\5H%\2\u0168\u0169")
        buf.write("\7\30\2\2\u0169\u016a\b \1\2\u016a\u016c\3\2\2\2\u016b")
        buf.write("\u0165\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2")
        buf.write("\u016d\u016e\3\2\2\2\u016e?\3\2\2\2\u016f\u016d\3\2\2")
        buf.write("\2\u0170\u0171\7\31\2\2\u0171\u0172\7\n\2\2\u0172\u0173")
        buf.write("\5H%\2\u0173\u0174\7\13\2\2\u0174\u0175\b!\1\2\u0175\u0183")
        buf.write("\3\2\2\2\u0176\u0177\7\32\2\2\u0177\u0178\7\n\2\2\u0178")
        buf.write("\u0179\5H%\2\u0179\u017a\7\13\2\2\u017a\u017b\b!\1\2\u017b")
        buf.write("\u0183\3\2\2\2\u017c\u017d\5\b\5\2\u017d\u017e\7\n\2\2")
        buf.write("\u017e\u017f\5B\"\2\u017f\u0180\7\13\2\2\u0180\u0181\b")
        buf.write("!\1\2\u0181\u0183\3\2\2\2\u0182\u0170\3\2\2\2\u0182\u0176")
        buf.write("\3\2\2\2\u0182\u017c\3\2\2\2\u0183A\3\2\2\2\u0184\u0185")
        buf.write("\5H%\2\u0185\u0186\5D#\2\u0186\u0187\b\"\1\2\u0187\u018a")
        buf.write("\3\2\2\2\u0188\u018a\b\"\1\2\u0189\u0184\3\2\2\2\u0189")
        buf.write("\u0188\3\2\2\2\u018aC\3\2\2\2\u018b\u018c\7\16\2\2\u018c")
        buf.write("\u018d\5H%\2\u018d\u018e\5D#\2\u018e\u018f\b#\1\2\u018f")
        buf.write("\u0192\3\2\2\2\u0190\u0192\b#\1\2\u0191\u018b\3\2\2\2")
        buf.write("\u0191\u0190\3\2\2\2\u0192E\3\2\2\2\u0193\u0194\7\n\2")
        buf.write("\2\u0194\u0195\5\16\b\2\u0195\u0196\7\13\2\2\u0196\u0197")
        buf.write("\5\66\34\2\u0197\u0198\b$\1\2\u0198G\3\2\2\2\u0199\u019a")
        buf.write("\b%\1\2\u019a\u019b\5J&\2\u019b\u019c\b%\1\2\u019c\u01a9")
        buf.write("\3\2\2\2\u019d\u019e\f\4\2\2\u019e\u019f\5T+\2\u019f\u01a0")
        buf.write("\7&\2\2\u01a0\u01a1\b%\1\2\u01a1\u01a8\3\2\2\2\u01a2\u01a3")
        buf.write("\f\3\2\2\u01a3\u01a4\5R*\2\u01a4\u01a5\5J&\2\u01a5\u01a6")
        buf.write("\b%\1\2\u01a6\u01a8\3\2\2\2\u01a7\u019d\3\2\2\2\u01a7")
        buf.write("\u01a2\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01a9\u01aa\3\2\2\2\u01aaI\3\2\2\2\u01ab\u01a9\3\2\2")
        buf.write("\2\u01ac\u01ad\b&\1\2\u01ad\u01ae\5\66\34\2\u01ae\u01af")
        buf.write("\b&\1\2\u01af\u01b7\3\2\2\2\u01b0\u01b1\f\3\2\2\u01b1")
        buf.write("\u01b2\5P)\2\u01b2\u01b3\5\66\34\2\u01b3\u01b4\b&\1\2")
        buf.write("\u01b4\u01b6\3\2\2\2\u01b5\u01b0\3\2\2\2\u01b6\u01b9\3")
        buf.write("\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8K")
        buf.write("\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01bb\5H%\2\u01bb\u01bc")
        buf.write("\5N(\2\u01bc\u01bd\5H%\2\u01bd\u01be\b\'\1\2\u01beM\3")
        buf.write("\2\2\2\u01bf\u01c0\t\2\2\2\u01c0O\3\2\2\2\u01c1\u01c2")
        buf.write("\t\3\2\2\u01c2Q\3\2\2\2\u01c3\u01c4\t\4\2\2\u01c4S\3\2")
        buf.write("\2\2\u01c5\u01c6\t\5\2\2\u01c6U\3\2\2\2\32dj\u0083\u008a")
        buf.write("\u0091\u00a0\u00b3\u00bb\u00c6\u00d2\u00e3\u00f7\u0104")
        buf.write("\u011c\u012d\u014a\u015c\u016d\u0182\u0189\u0191\u01a7")
        buf.write("\u01a9\u01b7")
        return buf.getvalue()


class MicroCParser ( Parser ):

    grammarFileName = "MicroC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'string'", "'='", "'*'", "'int'", 
                     "'float'", "'void'", "'('", "')'", "'{'", "'}'", "','", 
                     "'read'", "'print'", "'return'", "'if'", "'else'", 
                     "'while'", "'-'", "'&'", "'['", "']'", "'malloc'", 
                     "'free'", "'<'", "'<='", "'>='", "'=='", "'!='", "'>'", 
                     "'/'", "'+'", "'<<'", "'>>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "INT_LITERAL", "FLOAT_LITERAL", "STR_LITERAL", "COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_var_decls = 2
    RULE_ident = 3
    RULE_var_decl = 4
    RULE_str_decl = 5
    RULE_my_type = 6
    RULE_base_type = 7
    RULE_func_type = 8
    RULE_func_decl = 9
    RULE_functions = 10
    RULE_function = 11
    RULE_params = 12
    RULE_params_rest = 13
    RULE_param = 14
    RULE_statements = 15
    RULE_statement = 16
    RULE_base_stmt = 17
    RULE_read_stmt = 18
    RULE_print_stmt = 19
    RULE_return_stmt = 20
    RULE_assign_stmt = 21
    RULE_lhs = 22
    RULE_if_stmt = 23
    RULE_while_stmt = 24
    RULE_lval = 25
    RULE_primary = 26
    RULE_unaryminus_expr = 27
    RULE_ptr_expr = 28
    RULE_addr_of_expr = 29
    RULE_array_expr = 30
    RULE_call_expr = 31
    RULE_arg_list = 32
    RULE_args_rest = 33
    RULE_cast_expr = 34
    RULE_expr = 35
    RULE_term = 36
    RULE_cond = 37
    RULE_cmpop = 38
    RULE_mulop = 39
    RULE_addop = 40
    RULE_shiftop = 41

    ruleNames =  [ "program", "decls", "var_decls", "ident", "var_decl", 
                   "str_decl", "my_type", "base_type", "func_type", "func_decl", 
                   "functions", "function", "params", "params_rest", "param", 
                   "statements", "statement", "base_stmt", "read_stmt", 
                   "print_stmt", "return_stmt", "assign_stmt", "lhs", "if_stmt", 
                   "while_stmt", "lval", "primary", "unaryminus_expr", "ptr_expr", 
                   "addr_of_expr", "array_expr", "call_expr", "arg_list", 
                   "args_rest", "cast_expr", "expr", "term", "cond", "cmpop", 
                   "mulop", "addop", "shiftop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    IDENTIFIER=35
    INT_LITERAL=36
    FLOAT_LITERAL=37
    STR_LITERAL=38
    COMMENT=39
    WS=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    def setSymbolTable(self, st: SymbolTable):
      self.st = st

    def getSymbolTable(self) -> SymbolTable:
      return self.st

    def setAST(self, node: ASTNode):
      self.ast = node

    def getAST(self) -> ASTNode:
      return self.ast

    def addParams(self, types: List[Scope.Type], names: List[str]):
      for i in reversed(range(len(types))):
        self.st.addArgument(types[i], names[i])




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._functions = None # FunctionsContext

        def decls(self):
            return self.getTypedRuleContext(MicroCParser.DeclsContext,0)


        def functions(self):
            return self.getTypedRuleContext(MicroCParser.FunctionsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MicroCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.decls()
            self.state = 85
            localctx._functions = self.functions()
            self.setAST(localctx._functions.node);
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MicroCParser.Var_declContext,0)


        def decls(self):
            return self.getTypedRuleContext(MicroCParser.DeclsContext,0)


        def str_decl(self):
            return self.getTypedRuleContext(MicroCParser.Str_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MicroCParser.Func_declContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls" ):
                listener.enterDecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls" ):
                listener.exitDecls(self)




    def decls(self):

        localctx = MicroCParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.var_decl()
                self.state = 89
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.str_decl()
                self.state = 92
                self.decls()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.func_decl()
                self.state = 95
                self.decls()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MicroCParser.Var_declContext,0)


        def var_decls(self):
            return self.getTypedRuleContext(MicroCParser.Var_declsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_var_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decls" ):
                listener.enterVar_decls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decls" ):
                listener.exitVar_decls(self)




    def var_decls(self):

        localctx = MicroCParser.Var_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decls)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4, MicroCParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.var_decl()
                self.state = 101
                self.var_decls()
                pass
            elif token in [MicroCParser.T__3, MicroCParser.T__10, MicroCParser.T__12, MicroCParser.T__13, MicroCParser.T__14, MicroCParser.T__15, MicroCParser.T__17, MicroCParser.T__22, MicroCParser.T__23, MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MicroCParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)




    def ident(self):

        localctx = MicroCParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ident)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(MicroCParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._my_type = None # My_typeContext
            self._ident = None # IdentContext

        def my_type(self):
            return self.getTypedRuleContext(MicroCParser.My_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)




    def var_decl(self):

        localctx = MicroCParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            localctx._my_type = self.my_type(0)
            self.state = 109
            localctx._ident = self.ident()
            self.state = 110
            self.match(MicroCParser.T__0)
            self.st.addVariable(localctx._my_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ident = None # IdentContext
            self.val = None # Token

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def STR_LITERAL(self):
            return self.getToken(MicroCParser.STR_LITERAL, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_str_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_decl" ):
                listener.enterStr_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_decl" ):
                listener.exitStr_decl(self)




    def str_decl(self):

        localctx = MicroCParser.Str_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_str_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(MicroCParser.T__1)
            self.state = 114
            localctx._ident = self.ident()
            self.state = 115
            self.match(MicroCParser.T__2)
            self.state = 116
            localctx.val = self.match(MicroCParser.STR_LITERAL)
            self.state = 117
            self.match(MicroCParser.T__0)
            self.st.addVariable(Scope.Type(Scope.InnerType.STRING), (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), (None if localctx.val is None else localctx.val.text));
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class My_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None
            self.t1 = None # My_typeContext
            self._base_type = None # Base_typeContext

        def base_type(self):
            return self.getTypedRuleContext(MicroCParser.Base_typeContext,0)


        def my_type(self):
            return self.getTypedRuleContext(MicroCParser.My_typeContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_my_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMy_type" ):
                listener.enterMy_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMy_type" ):
                listener.exitMy_type(self)



    def my_type(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.My_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_my_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            localctx._base_type = self.base_type()
            localctx.t =  localctx._base_type.t
            self._ctx.stop = self._input.LT(-1)
            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MicroCParser.My_typeContext(self, _parentctx, _parentState)
                    localctx.t1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_my_type)
                    self.state = 124
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 125
                    self.match(MicroCParser.T__3)
                    localctx.t =  Scope.Type.pointerToType(localctx.t1.t) 
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Base_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None


        def getRuleIndex(self):
            return MicroCParser.RULE_base_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_type" ):
                listener.enterBase_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_type" ):
                listener.exitBase_type(self)




    def base_type(self):

        localctx = MicroCParser.Base_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_base_type)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(MicroCParser.T__4)
                localctx.t =  Scope.Type(Scope.InnerType.INT)
                pass
            elif token in [MicroCParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(MicroCParser.T__5)
                localctx.t =  Scope.Type(Scope.InnerType.FLOAT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None
            self._my_type = None # My_typeContext

        def my_type(self):
            return self.getTypedRuleContext(MicroCParser.My_typeContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_func_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_type" ):
                listener.enterFunc_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_type" ):
                listener.exitFunc_type(self)




    def func_type(self):

        localctx = MicroCParser.Func_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_type)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4, MicroCParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                localctx._my_type = self.my_type(0)
                localctx.t =  localctx._my_type.t
                pass
            elif token in [MicroCParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(MicroCParser.T__6)
                localctx.t =  Scope.Type(Scope.InnerType.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._func_type = None # Func_typeContext
            self._ident = None # IdentContext
            self._params = None # ParamsContext

        def func_type(self):
            return self.getTypedRuleContext(MicroCParser.Func_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def params(self):
            return self.getTypedRuleContext(MicroCParser.ParamsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_func_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decl" ):
                listener.enterFunc_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decl" ):
                listener.exitFunc_decl(self)




    def func_decl(self):

        localctx = MicroCParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            localctx._func_type = self.func_type()
            self.state = 146
            localctx._ident = self.ident()
            self.state = 147
            self.match(MicroCParser.T__7)
            self.state = 148
            localctx._params = self.params()
            self.state = 149
            self.match(MicroCParser.T__8)
            self.state = 150
            self.match(MicroCParser.T__0)
            self.st.addFunction(localctx._func_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), localctx._params.types);
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._function = None # FunctionContext
            self._functions = None # FunctionsContext

        def function(self):
            return self.getTypedRuleContext(MicroCParser.FunctionContext,0)


        def functions(self):
            return self.getTypedRuleContext(MicroCParser.FunctionsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)




    def functions(self):

        localctx = MicroCParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functions)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4, MicroCParser.T__5, MicroCParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                localctx._function = self.function()
                self.state = 154
                localctx._functions = self.functions()
                localctx.node =  FunctionListNode(localctx._function.node, localctx._functions.node)
                pass
            elif token in [MicroCParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                localctx.node =  FunctionListNode()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._func_type = None # Func_typeContext
            self._ident = None # IdentContext
            self._params = None # ParamsContext
            self._statements = None # StatementsContext

        def func_type(self):
            return self.getTypedRuleContext(MicroCParser.Func_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def params(self):
            return self.getTypedRuleContext(MicroCParser.ParamsContext,0)


        def var_decls(self):
            return self.getTypedRuleContext(MicroCParser.Var_declsContext,0)


        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = MicroCParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            localctx._func_type = self.func_type()
            self.state = 161
            localctx._ident = self.ident()
            self.state = 162
            self.match(MicroCParser.T__7)
            self.state = 163
            localctx._params = self.params()
            self.state = 164
            self.match(MicroCParser.T__8)

            # Add FunctionSymbolTable entry to global scope
            ste = self.st.getSymbolTableEntry((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
            if ste is None or not ste.isDefined():
              self.st.addFunction(localctx._func_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), localctx._params.types);          
              ste = self.st.getSymbolTableEntry((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
              ste.setDefined(True);
            else:
              raise Exception("Function already defined");
            self.st.pushScope((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
            self.addParams(localctx._params.types, localctx._params.names);

            self.state = 166
            self.match(MicroCParser.T__9)
            self.state = 167
            self.var_decls()
            self.state = 168
            localctx._statements = self.statements()
            self.state = 169
            self.match(MicroCParser.T__10)

            # Create FunctionNode
            funcScope = self.st.currentScope();
            localctx.node =  FunctionNode(localctx._statements.node, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), funcScope)

            # Done with this scope, so pop the scope
            self.st.popScope();

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.names = None
            self.types = None
            self._param = None # ParamContext
            self._params_rest = None # Params_restContext

        def param(self):
            return self.getTypedRuleContext(MicroCParser.ParamContext,0)


        def params_rest(self):
            return self.getTypedRuleContext(MicroCParser.Params_restContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = MicroCParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_params)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4, MicroCParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                localctx._param = self.param()
                self.state = 173
                localctx._params_rest = self.params_rest()

                localctx.names =  []
                localctx.types =  []
                localctx.names.append(localctx._param.name);
                localctx.names.extend(localctx._params_rest.names);
                localctx.types.append(localctx._param.param_type);
                localctx.types.extend(localctx._params_rest.types);

                pass
            elif token in [MicroCParser.T__8]:
                self.enterOuterAlt(localctx, 2)

                localctx.names =  []
                localctx.types =  []

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.names = None
            self.types = None
            self._param = None # ParamContext
            self._params_rest = None # Params_restContext

        def param(self):
            return self.getTypedRuleContext(MicroCParser.ParamContext,0)


        def params_rest(self):
            return self.getTypedRuleContext(MicroCParser.Params_restContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_params_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams_rest" ):
                listener.enterParams_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams_rest" ):
                listener.exitParams_rest(self)




    def params_rest(self):

        localctx = MicroCParser.Params_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_params_rest)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(MicroCParser.T__11)
                self.state = 180
                localctx._param = self.param()
                self.state = 181
                localctx._params_rest = self.params_rest()

                localctx.names =  []
                localctx.types =  []
                localctx.names.append(localctx._param.name);
                localctx.names.extend(localctx._params_rest.names);
                localctx.types.append(localctx._param.param_type);
                localctx.types.extend(localctx._params_rest.types);

                pass
            elif token in [MicroCParser.T__8]:
                self.enterOuterAlt(localctx, 2)

                localctx.names =  []
                localctx.types =  []

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None
            self.param_type = None
            self._my_type = None # My_typeContext
            self._ident = None # IdentContext

        def my_type(self):
            return self.getTypedRuleContext(MicroCParser.My_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = MicroCParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            localctx._my_type = self.my_type(0)
            self.state = 188
            localctx._ident = self.ident()

            localctx.name =  (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop))
            localctx.param_type =  localctx._my_type.t

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._statement = None # StatementContext
            self.s = None # StatementsContext

        def statement(self):
            return self.getTypedRuleContext(MicroCParser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = MicroCParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statements)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3, MicroCParser.T__12, MicroCParser.T__13, MicroCParser.T__14, MicroCParser.T__15, MicroCParser.T__17, MicroCParser.T__22, MicroCParser.T__23, MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                localctx._statement = self.statement()
                self.state = 192
                localctx.s = self.statements()
                localctx.node =  StatementListNode(localctx._statement.node, localctx.s.node.getStatements())
                pass
            elif token in [MicroCParser.T__10]:
                self.enterOuterAlt(localctx, 2)
                localctx.node =  StatementListNode()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._base_stmt = None # Base_stmtContext
            self._if_stmt = None # If_stmtContext
            self._while_stmt = None # While_stmtContext

        def base_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Base_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MicroCParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MicroCParser.While_stmtContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MicroCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statement)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3, MicroCParser.T__12, MicroCParser.T__13, MicroCParser.T__14, MicroCParser.T__22, MicroCParser.T__23, MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                localctx._base_stmt = self.base_stmt()
                self.state = 199
                self.match(MicroCParser.T__0)
                localctx.node =  localctx._base_stmt.node
                pass
            elif token in [MicroCParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                localctx._if_stmt = self.if_stmt()
                localctx.node =  localctx._if_stmt.node
                pass
            elif token in [MicroCParser.T__17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                localctx._while_stmt = self.while_stmt()
                localctx.node = localctx._while_stmt.node
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._assign_stmt = None # Assign_stmtContext
            self._read_stmt = None # Read_stmtContext
            self._print_stmt = None # Print_stmtContext
            self._return_stmt = None # Return_stmtContext
            self._call_expr = None # Call_exprContext

        def assign_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Assign_stmtContext,0)


        def read_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Read_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Print_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Return_stmtContext,0)


        def call_expr(self):
            return self.getTypedRuleContext(MicroCParser.Call_exprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_base_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_stmt" ):
                listener.enterBase_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_stmt" ):
                listener.exitBase_stmt(self)




    def base_stmt(self):

        localctx = MicroCParser.Base_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_base_stmt)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                localctx._assign_stmt = self.assign_stmt()
                localctx.node =  localctx._assign_stmt.node
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                localctx._read_stmt = self.read_stmt()
                localctx.node =  localctx._read_stmt.node
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                localctx._print_stmt = self.print_stmt()
                localctx.node =  localctx._print_stmt.node
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
                localctx._return_stmt = self.return_stmt()
                localctx.node =  localctx._return_stmt.node
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 222
                localctx._call_expr = self.call_expr()
                localctx.node =  localctx._call_expr.node
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_read_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_stmt" ):
                listener.enterRead_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_stmt" ):
                listener.exitRead_stmt(self)




    def read_stmt(self):

        localctx = MicroCParser.Read_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_read_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(MicroCParser.T__12)
            self.state = 228
            self.match(MicroCParser.T__7)
            self.state = 229
            localctx._ident = self.ident()
            self.state = 230
            self.match(MicroCParser.T__8)
            localctx.node =  ReadNode(VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop))))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)




    def print_stmt(self):

        localctx = MicroCParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MicroCParser.T__13)
            self.state = 234
            self.match(MicroCParser.T__7)
            self.state = 235
            localctx._expr = self.expr(0)
            self.state = 236
            self.match(MicroCParser.T__8)
            localctx.node =  WriteNode(localctx._expr.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)




    def return_stmt(self):

        localctx = MicroCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_return_stmt)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(MicroCParser.T__14)
                self.state = 240
                localctx._expr = self.expr(0)
                localctx.node =  ReturnNode(localctx._expr.node, self.st.getFunctionSymbol(self.st.currentScope().getName()))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.match(MicroCParser.T__14)
                localctx.node =  ReturnNode(None, self.st.getFunctionSymbol(self.st.currentScope().getName()))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._lhs = None # LhsContext
            self._expr = None # ExprContext

        def lhs(self):
            return self.getTypedRuleContext(MicroCParser.LhsContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_assign_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)




    def assign_stmt(self):

        localctx = MicroCParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            localctx._lhs = self.lhs()
            self.state = 248
            self.match(MicroCParser.T__2)
            self.state = 249
            localctx._expr = self.expr(0)
            localctx.node =  AssignNode(localctx._lhs.node, localctx._expr.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._lval = None # LvalContext
            self._array_expr = None # Array_exprContext

        def lval(self):
            return self.getTypedRuleContext(MicroCParser.LvalContext,0)


        def array_expr(self):
            return self.getTypedRuleContext(MicroCParser.Array_exprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_lhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLhs" ):
                listener.enterLhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLhs" ):
                listener.exitLhs(self)




    def lhs(self):

        localctx = MicroCParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_lhs)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                localctx._lval = self.lval()
                localctx.node =  localctx._lval.node
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                localctx._array_expr = self.array_expr(0)
                localctx.node =  localctx._array_expr.node
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._cond = None # CondContext
            self._statements = None # StatementsContext
            self.ts = None # StatementsContext
            self.es = None # StatementsContext

        def cond(self):
            return self.getTypedRuleContext(MicroCParser.CondContext,0)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MicroCParser.StatementsContext)
            else:
                return self.getTypedRuleContext(MicroCParser.StatementsContext,i)


        def getRuleIndex(self):
            return MicroCParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)




    def if_stmt(self):

        localctx = MicroCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_stmt)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(MicroCParser.T__15)
                self.state = 261
                self.match(MicroCParser.T__7)
                self.state = 262
                localctx._cond = self.cond()
                self.state = 263
                self.match(MicroCParser.T__8)
                self.state = 264
                self.match(MicroCParser.T__9)
                self.state = 265
                localctx._statements = self.statements()
                self.state = 266
                self.match(MicroCParser.T__10)
                localctx.node =  IfStatementNode(localctx._cond.node, StatementListNode(None, localctx._statements.node.getStatements()), None)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.match(MicroCParser.T__15)
                self.state = 270
                self.match(MicroCParser.T__7)
                self.state = 271
                localctx._cond = self.cond()
                self.state = 272
                self.match(MicroCParser.T__8)
                self.state = 273
                self.match(MicroCParser.T__9)
                self.state = 274
                localctx.ts = self.statements()
                self.state = 275
                self.match(MicroCParser.T__10)
                self.state = 276
                self.match(MicroCParser.T__16)
                self.state = 277
                self.match(MicroCParser.T__9)
                self.state = 278
                localctx.es = self.statements()
                self.state = 279
                self.match(MicroCParser.T__10)
                localctx.node =  IfStatementNode(localctx._cond.node, StatementListNode(None, localctx.ts.node.getStatements()), StatementListNode(None, localctx.es.node.getStatements()))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._cond = None # CondContext
            self._statements = None # StatementsContext

        def cond(self):
            return self.getTypedRuleContext(MicroCParser.CondContext,0)


        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)




    def while_stmt(self):

        localctx = MicroCParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(MicroCParser.T__17)
            self.state = 285
            self.match(MicroCParser.T__7)
            self.state = 286
            localctx._cond = self.cond()
            self.state = 287
            self.match(MicroCParser.T__8)
            self.state = 288
            self.match(MicroCParser.T__9)
            self.state = 289
            localctx._statements = self.statements()
            self.state = 290
            self.match(MicroCParser.T__10)
            localctx.node =  WhileNode(localctx._cond.node, StatementListNode(localctx._statements.node))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext
            self._ptr_expr = None # Ptr_exprContext

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def ptr_expr(self):
            return self.getTypedRuleContext(MicroCParser.Ptr_exprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_lval

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLval" ):
                listener.enterLval(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLval" ):
                listener.exitLval(self)




    def lval(self):

        localctx = MicroCParser.LvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_lval)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                localctx._ident = self.ident()
                localctx.node =  VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)))
                pass
            elif token in [MicroCParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                localctx._ptr_expr = self.ptr_expr()
                localctx.node =  localctx._ptr_expr.node
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._lval = None # LvalContext
            self._cast_expr = None # Cast_exprContext
            self._addr_of_expr = None # Addr_of_exprContext
            self._expr = None # ExprContext
            self._unaryminus_expr = None # Unaryminus_exprContext
            self._call_expr = None # Call_exprContext
            self._array_expr = None # Array_exprContext
            self.il = None # Token
            self.fl = None # Token

        def lval(self):
            return self.getTypedRuleContext(MicroCParser.LvalContext,0)


        def cast_expr(self):
            return self.getTypedRuleContext(MicroCParser.Cast_exprContext,0)


        def addr_of_expr(self):
            return self.getTypedRuleContext(MicroCParser.Addr_of_exprContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def unaryminus_expr(self):
            return self.getTypedRuleContext(MicroCParser.Unaryminus_exprContext,0)


        def call_expr(self):
            return self.getTypedRuleContext(MicroCParser.Call_exprContext,0)


        def array_expr(self):
            return self.getTypedRuleContext(MicroCParser.Array_exprContext,0)


        def INT_LITERAL(self):
            return self.getToken(MicroCParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MicroCParser.FLOAT_LITERAL, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = MicroCParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_primary)
        try:
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                localctx._lval = self.lval()
                localctx.node =  localctx._lval.node
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                localctx._cast_expr = self.cast_expr()
                localctx.node =  localctx._cast_expr.node
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 307
                localctx._addr_of_expr = self.addr_of_expr()
                localctx.node =  localctx._addr_of_expr.node
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 310
                self.match(MicroCParser.T__7)
                self.state = 311
                localctx._expr = self.expr(0)
                self.state = 312
                self.match(MicroCParser.T__8)
                localctx.node =  localctx._expr.node
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 315
                localctx._unaryminus_expr = self.unaryminus_expr()
                localctx.node =  localctx._unaryminus_expr.node
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 318
                localctx._call_expr = self.call_expr()
                localctx.node =  localctx._call_expr.node
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 321
                localctx._array_expr = self.array_expr(0)
                localctx.node =  localctx._array_expr.node
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 324
                localctx.il = self.match(MicroCParser.INT_LITERAL)
                localctx.node =  IntLitNode((None if localctx.il is None else localctx.il.text))
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 326
                localctx.fl = self.match(MicroCParser.FLOAT_LITERAL)
                localctx.node =  FloatLitNode((None if localctx.fl is None else localctx.fl.text))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unaryminus_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_unaryminus_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryminus_expr" ):
                listener.enterUnaryminus_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryminus_expr" ):
                listener.exitUnaryminus_expr(self)




    def unaryminus_expr(self):

        localctx = MicroCParser.Unaryminus_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_unaryminus_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(MicroCParser.T__18)
            self.state = 331
            localctx._expr = self.expr(0)
            localctx.node =  UnaryOpNode(localctx._expr.node, '-')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ptr_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._primary = None # PrimaryContext

        def primary(self):
            return self.getTypedRuleContext(MicroCParser.PrimaryContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_ptr_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPtr_expr" ):
                listener.enterPtr_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPtr_expr" ):
                listener.exitPtr_expr(self)




    def ptr_expr(self):

        localctx = MicroCParser.Ptr_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ptr_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(MicroCParser.T__3)
            self.state = 335
            localctx._primary = self.primary()
            localctx.node =  PtrDerefNode(localctx._primary.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Addr_of_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._lval = None # LvalContext
            self._array_expr = None # Array_exprContext

        def lval(self):
            return self.getTypedRuleContext(MicroCParser.LvalContext,0)


        def array_expr(self):
            return self.getTypedRuleContext(MicroCParser.Array_exprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_addr_of_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddr_of_expr" ):
                listener.enterAddr_of_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddr_of_expr" ):
                listener.exitAddr_of_expr(self)




    def addr_of_expr(self):

        localctx = MicroCParser.Addr_of_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_addr_of_expr)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(MicroCParser.T__19)
                self.state = 339
                localctx._lval = self.lval()
                localctx.node =  AddrOfNode(localctx._lval.node)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.match(MicroCParser.T__19)
                self.state = 343
                localctx._array_expr = self.array_expr(0)
                localctx.node =  AddrOfNode(localctx._array_expr.node)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.ae = None # Array_exprContext
            self._lval = None # LvalContext
            self._expr = None # ExprContext

        def lval(self):
            return self.getTypedRuleContext(MicroCParser.LvalContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def array_expr(self):
            return self.getTypedRuleContext(MicroCParser.Array_exprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_array_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_expr" ):
                listener.enterArray_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_expr" ):
                listener.exitArray_expr(self)



    def array_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.Array_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_array_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            localctx._lval = self.lval()
            self.state = 350
            self.match(MicroCParser.T__20)
            self.state = 351
            localctx._expr = self.expr(0)
            self.state = 352
            self.match(MicroCParser.T__21)
            localctx.node =  PtrDerefNode(BinaryOpNode(localctx._lval.node, BinaryOpNode(IntLitNode('4'), localctx._expr.node, '*'), '+'))
            self._ctx.stop = self._input.LT(-1)
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MicroCParser.Array_exprContext(self, _parentctx, _parentState)
                    localctx.ae = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_array_expr)
                    self.state = 355
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 356
                    self.match(MicroCParser.T__20)
                    self.state = 357
                    localctx._expr = self.expr(0)
                    self.state = 358
                    self.match(MicroCParser.T__21)
                    localctx.node =  PtrDerefNode(BinaryOpNode(localctx.ae.node, BinaryOpNode(IntLitNode('4'), localctx._expr.node, '*'), '+')) 
                self.state = 365
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext
            self._ident = None # IdentContext
            self._arg_list = None # Arg_listContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def arg_list(self):
            return self.getTypedRuleContext(MicroCParser.Arg_listContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_call_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_expr" ):
                listener.enterCall_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_expr" ):
                listener.exitCall_expr(self)




    def call_expr(self):

        localctx = MicroCParser.Call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_call_expr)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(MicroCParser.T__22)
                self.state = 367
                self.match(MicroCParser.T__7)
                self.state = 368
                localctx._expr = self.expr(0)
                self.state = 369
                self.match(MicroCParser.T__8)
                localctx.node =  MallocNode(localctx._expr.node)
                pass
            elif token in [MicroCParser.T__23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.match(MicroCParser.T__23)
                self.state = 373
                self.match(MicroCParser.T__7)
                self.state = 374
                localctx._expr = self.expr(0)
                self.state = 375
                self.match(MicroCParser.T__8)
                localctx.node =  FreeNode(localctx._expr.node)
                pass
            elif token in [MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                localctx._ident = self.ident()
                self.state = 379
                self.match(MicroCParser.T__7)
                self.state = 380
                localctx._arg_list = self.arg_list()
                self.state = 381
                self.match(MicroCParser.T__8)
                localctx.node =  CallNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), localctx._arg_list.args)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.args = None
            self._expr = None # ExprContext
            self._args_rest = None # Args_restContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def args_rest(self):
            return self.getTypedRuleContext(MicroCParser.Args_restContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)




    def arg_list(self):

        localctx = MicroCParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_arg_list)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3, MicroCParser.T__7, MicroCParser.T__18, MicroCParser.T__19, MicroCParser.T__22, MicroCParser.T__23, MicroCParser.IDENTIFIER, MicroCParser.INT_LITERAL, MicroCParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                localctx._expr = self.expr(0)
                self.state = 387
                localctx._args_rest = self.args_rest()

                localctx.args =  []
                localctx.args.append(localctx._expr.node);
                localctx.args.extend(localctx._args_rest.args);

                pass
            elif token in [MicroCParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                localctx.args =  []
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Args_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.args = None
            self._expr = None # ExprContext
            self._args_rest = None # Args_restContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def args_rest(self):
            return self.getTypedRuleContext(MicroCParser.Args_restContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_args_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs_rest" ):
                listener.enterArgs_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs_rest" ):
                listener.exitArgs_rest(self)




    def args_rest(self):

        localctx = MicroCParser.Args_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_args_rest)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.match(MicroCParser.T__11)
                self.state = 394
                localctx._expr = self.expr(0)
                self.state = 395
                localctx._args_rest = self.args_rest()

                localctx.args =  []
                localctx.args.append(localctx._expr.node);
                localctx.args.extend(localctx._args_rest.args);

                pass
            elif token in [MicroCParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                localctx.args =  []
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cast_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._my_type = None # My_typeContext
            self._primary = None # PrimaryContext

        def my_type(self):
            return self.getTypedRuleContext(MicroCParser.My_typeContext,0)


        def primary(self):
            return self.getTypedRuleContext(MicroCParser.PrimaryContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_cast_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCast_expr" ):
                listener.enterCast_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCast_expr" ):
                listener.exitCast_expr(self)




    def cast_expr(self):

        localctx = MicroCParser.Cast_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_cast_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(MicroCParser.T__7)
            self.state = 402
            localctx._my_type = self.my_type(0)
            self.state = 403
            self.match(MicroCParser.T__8)
            self.state = 404
            localctx._primary = self.primary()
            localctx.node = CastNode(localctx._my_type.t, localctx._primary.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExprContext
            self._term = None # TermContext
            self._shiftop = None # ShiftopContext
            self.il = None # Token
            self._addop = None # AddopContext

        def term(self):
            return self.getTypedRuleContext(MicroCParser.TermContext,0)


        def shiftop(self):
            return self.getTypedRuleContext(MicroCParser.ShiftopContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def INT_LITERAL(self):
            return self.getToken(MicroCParser.INT_LITERAL, 0)

        def addop(self):
            return self.getTypedRuleContext(MicroCParser.AddopContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            localctx._term = self.term(0)
            localctx.node =  localctx._term.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 421
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = MicroCParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 411
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 412
                        localctx._shiftop = self.shiftop()
                        self.state = 413
                        localctx.il = self.match(MicroCParser.INT_LITERAL)
                        localctx.node =  ShiftNode(localctx.e1.node, (None if localctx.il is None else localctx.il.text), (None if localctx._shiftop is None else self._input.getText(localctx._shiftop.start,localctx._shiftop.stop)))
                        pass

                    elif la_ == 2:
                        localctx = MicroCParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 416
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 417
                        localctx._addop = self.addop()
                        self.state = 418
                        localctx._term = self.term(0)
                        localctx.node =  BinaryOpNode(localctx.e1.node, localctx._term.node, (None if localctx._addop is None else self._input.getText(localctx._addop.start,localctx._addop.stop)))
                        pass

             
                self.state = 425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.t1 = None # TermContext
            self._primary = None # PrimaryContext
            self._mulop = None # MulopContext

        def primary(self):
            return self.getTypedRuleContext(MicroCParser.PrimaryContext,0)


        def mulop(self):
            return self.getTypedRuleContext(MicroCParser.MulopContext,0)


        def term(self):
            return self.getTypedRuleContext(MicroCParser.TermContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            localctx._primary = self.primary()
            localctx.node =  localctx._primary.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 437
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MicroCParser.TermContext(self, _parentctx, _parentState)
                    localctx.t1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 430
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 431
                    localctx._mulop = self.mulop()
                    self.state = 432
                    localctx._primary = self.primary()
                    localctx.node =  BinaryOpNode(localctx.t1.node, localctx._primary.node, (None if localctx._mulop is None else self._input.getText(localctx._mulop.start,localctx._mulop.stop))) 
                self.state = 439
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExprContext
            self._cmpop = None # CmpopContext
            self.e2 = None # ExprContext

        def cmpop(self):
            return self.getTypedRuleContext(MicroCParser.CmpopContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MicroCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MicroCParser.ExprContext,i)


        def getRuleIndex(self):
            return MicroCParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = MicroCParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            localctx.e1 = self.expr(0)
            self.state = 441
            localctx._cmpop = self.cmpop()
            self.state = 442
            localctx.e2 = self.expr(0)
            localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, (None if localctx._cmpop is None else self._input.getText(localctx._cmpop.start,localctx._cmpop.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmpopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_cmpop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmpop" ):
                listener.enterCmpop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmpop" ):
                listener.exitCmpop(self)




    def cmpop(self):

        localctx = MicroCParser.CmpopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_cmpop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MicroCParser.T__24) | (1 << MicroCParser.T__25) | (1 << MicroCParser.T__26) | (1 << MicroCParser.T__27) | (1 << MicroCParser.T__28) | (1 << MicroCParser.T__29))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_mulop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulop" ):
                listener.enterMulop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulop" ):
                listener.exitMulop(self)




    def mulop(self):

        localctx = MicroCParser.MulopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_mulop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            _la = self._input.LA(1)
            if not(_la==MicroCParser.T__3 or _la==MicroCParser.T__30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_addop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddop" ):
                listener.enterAddop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddop" ):
                listener.exitAddop(self)




    def addop(self):

        localctx = MicroCParser.AddopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_addop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            _la = self._input.LA(1)
            if not(_la==MicroCParser.T__18 or _la==MicroCParser.T__31):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShiftopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_shiftop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShiftop" ):
                listener.enterShiftop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShiftop" ):
                listener.exitShiftop(self)




    def shiftop(self):

        localctx = MicroCParser.ShiftopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_shiftop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            _la = self._input.LA(1)
            if not(_la==MicroCParser.T__32 or _la==MicroCParser.T__33):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.my_type_sempred
        self._predicates[30] = self.array_expr_sempred
        self._predicates[35] = self.expr_sempred
        self._predicates[36] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def my_type_sempred(self, localctx:My_typeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def array_expr_sempred(self, localctx:Array_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




