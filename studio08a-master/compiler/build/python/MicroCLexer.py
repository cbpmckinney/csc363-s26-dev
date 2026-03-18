# Generated from python/MicroC.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*")
        buf.write("\u010a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3$\3$\5$\u00ce\n$\3$\3$\3$\7$\u00d3")
        buf.write("\n$\f$\16$\u00d6\13$\3%\6%\u00d9\n%\r%\16%\u00da\3&\7")
        buf.write("&\u00de\n&\f&\16&\u00e1\13&\3&\3&\6&\u00e5\n&\r&\16&\u00e6")
        buf.write("\3\'\3\'\7\'\u00eb\n\'\f\'\16\'\u00ee\13\'\3\'\3\'\3(")
        buf.write("\3(\3(\3(\7(\u00f6\n(\f(\16(\u00f9\13(\3(\3(\3(\3(\3(")
        buf.write("\3)\6)\u0101\n)\r)\16)\u0102\3)\3)\3*\3*\3+\3+\3\u00f7")
        buf.write("\2,\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S\2U\2\3\2\5\3\2$$\5\2\13\f\17\17\"\"\4\2C\\c|\2")
        buf.write("\u0111\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\3W")
        buf.write("\3\2\2\2\5Y\3\2\2\2\7`\3\2\2\2\tb\3\2\2\2\13d\3\2\2\2")
        buf.write("\rh\3\2\2\2\17n\3\2\2\2\21s\3\2\2\2\23u\3\2\2\2\25w\3")
        buf.write("\2\2\2\27y\3\2\2\2\31{\3\2\2\2\33}\3\2\2\2\35\u0082\3")
        buf.write("\2\2\2\37\u0088\3\2\2\2!\u008f\3\2\2\2#\u0092\3\2\2\2")
        buf.write("%\u0097\3\2\2\2\'\u009d\3\2\2\2)\u009f\3\2\2\2+\u00a1")
        buf.write("\3\2\2\2-\u00a3\3\2\2\2/\u00a5\3\2\2\2\61\u00ac\3\2\2")
        buf.write("\2\63\u00b1\3\2\2\2\65\u00b3\3\2\2\2\67\u00b6\3\2\2\2")
        buf.write("9\u00b9\3\2\2\2;\u00bc\3\2\2\2=\u00bf\3\2\2\2?\u00c1\3")
        buf.write("\2\2\2A\u00c3\3\2\2\2C\u00c5\3\2\2\2E\u00c8\3\2\2\2G\u00cd")
        buf.write("\3\2\2\2I\u00d8\3\2\2\2K\u00df\3\2\2\2M\u00e8\3\2\2\2")
        buf.write("O\u00f1\3\2\2\2Q\u0100\3\2\2\2S\u0106\3\2\2\2U\u0108\3")
        buf.write("\2\2\2WX\7=\2\2X\4\3\2\2\2YZ\7u\2\2Z[\7v\2\2[\\\7t\2\2")
        buf.write("\\]\7k\2\2]^\7p\2\2^_\7i\2\2_\6\3\2\2\2`a\7?\2\2a\b\3")
        buf.write("\2\2\2bc\7,\2\2c\n\3\2\2\2de\7k\2\2ef\7p\2\2fg\7v\2\2")
        buf.write("g\f\3\2\2\2hi\7h\2\2ij\7n\2\2jk\7q\2\2kl\7c\2\2lm\7v\2")
        buf.write("\2m\16\3\2\2\2no\7x\2\2op\7q\2\2pq\7k\2\2qr\7f\2\2r\20")
        buf.write("\3\2\2\2st\7*\2\2t\22\3\2\2\2uv\7+\2\2v\24\3\2\2\2wx\7")
        buf.write("}\2\2x\26\3\2\2\2yz\7\177\2\2z\30\3\2\2\2{|\7.\2\2|\32")
        buf.write("\3\2\2\2}~\7t\2\2~\177\7g\2\2\177\u0080\7c\2\2\u0080\u0081")
        buf.write("\7f\2\2\u0081\34\3\2\2\2\u0082\u0083\7r\2\2\u0083\u0084")
        buf.write("\7t\2\2\u0084\u0085\7k\2\2\u0085\u0086\7p\2\2\u0086\u0087")
        buf.write("\7v\2\2\u0087\36\3\2\2\2\u0088\u0089\7t\2\2\u0089\u008a")
        buf.write("\7g\2\2\u008a\u008b\7v\2\2\u008b\u008c\7w\2\2\u008c\u008d")
        buf.write("\7t\2\2\u008d\u008e\7p\2\2\u008e \3\2\2\2\u008f\u0090")
        buf.write("\7k\2\2\u0090\u0091\7h\2\2\u0091\"\3\2\2\2\u0092\u0093")
        buf.write("\7g\2\2\u0093\u0094\7n\2\2\u0094\u0095\7u\2\2\u0095\u0096")
        buf.write("\7g\2\2\u0096$\3\2\2\2\u0097\u0098\7y\2\2\u0098\u0099")
        buf.write("\7j\2\2\u0099\u009a\7k\2\2\u009a\u009b\7n\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c&\3\2\2\2\u009d\u009e\7/\2\2\u009e(\3\2\2")
        buf.write("\2\u009f\u00a0\7(\2\2\u00a0*\3\2\2\2\u00a1\u00a2\7]\2")
        buf.write("\2\u00a2,\3\2\2\2\u00a3\u00a4\7_\2\2\u00a4.\3\2\2\2\u00a5")
        buf.write("\u00a6\7o\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8\7n\2\2\u00a8")
        buf.write("\u00a9\7n\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab\7e\2\2\u00ab")
        buf.write("\60\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae\7t\2\2\u00ae")
        buf.write("\u00af\7g\2\2\u00af\u00b0\7g\2\2\u00b0\62\3\2\2\2\u00b1")
        buf.write("\u00b2\7>\2\2\u00b2\64\3\2\2\2\u00b3\u00b4\7>\2\2\u00b4")
        buf.write("\u00b5\7?\2\2\u00b5\66\3\2\2\2\u00b6\u00b7\7@\2\2\u00b7")
        buf.write("\u00b8\7?\2\2\u00b88\3\2\2\2\u00b9\u00ba\7?\2\2\u00ba")
        buf.write("\u00bb\7?\2\2\u00bb:\3\2\2\2\u00bc\u00bd\7#\2\2\u00bd")
        buf.write("\u00be\7?\2\2\u00be<\3\2\2\2\u00bf\u00c0\7@\2\2\u00c0")
        buf.write(">\3\2\2\2\u00c1\u00c2\7\61\2\2\u00c2@\3\2\2\2\u00c3\u00c4")
        buf.write("\7-\2\2\u00c4B\3\2\2\2\u00c5\u00c6\7>\2\2\u00c6\u00c7")
        buf.write("\7>\2\2\u00c7D\3\2\2\2\u00c8\u00c9\7@\2\2\u00c9\u00ca")
        buf.write("\7@\2\2\u00caF\3\2\2\2\u00cb\u00ce\5S*\2\u00cc\u00ce\7")
        buf.write("a\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00d4")
        buf.write("\3\2\2\2\u00cf\u00d3\5S*\2\u00d0\u00d3\5U+\2\u00d1\u00d3")
        buf.write("\7a\2\2\u00d2\u00cf\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5H\3\2\2\2\u00d6\u00d4\3\2\2")
        buf.write("\2\u00d7\u00d9\5U+\2\u00d8\u00d7\3\2\2\2\u00d9\u00da\3")
        buf.write("\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00dbJ")
        buf.write("\3\2\2\2\u00dc\u00de\5U+\2\u00dd\u00dc\3\2\2\2\u00de\u00e1")
        buf.write("\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0")
        buf.write("\u00e2\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e4\7\60\2")
        buf.write("\2\u00e3\u00e5\5U+\2\u00e4\u00e3\3\2\2\2\u00e5\u00e6\3")
        buf.write("\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7L")
        buf.write("\3\2\2\2\u00e8\u00ec\7$\2\2\u00e9\u00eb\n\2\2\2\u00ea")
        buf.write("\u00e9\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2")
        buf.write("\u00ec\u00ed\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00ec\3")
        buf.write("\2\2\2\u00ef\u00f0\7$\2\2\u00f0N\3\2\2\2\u00f1\u00f2\7")
        buf.write("\61\2\2\u00f2\u00f3\7,\2\2\u00f3\u00f7\3\2\2\2\u00f4\u00f6")
        buf.write("\13\2\2\2\u00f5\u00f4\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7")
        buf.write("\u00f8\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00fa\3\2\2\2")
        buf.write("\u00f9\u00f7\3\2\2\2\u00fa\u00fb\7,\2\2\u00fb\u00fc\7")
        buf.write("\61\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\b(\2\2\u00feP")
        buf.write("\3\2\2\2\u00ff\u0101\t\3\2\2\u0100\u00ff\3\2\2\2\u0101")
        buf.write("\u0102\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2")
        buf.write("\u0103\u0104\3\2\2\2\u0104\u0105\b)\2\2\u0105R\3\2\2\2")
        buf.write("\u0106\u0107\t\4\2\2\u0107T\3\2\2\2\u0108\u0109\4\62;")
        buf.write("\2\u0109V\3\2\2\2\f\2\u00cd\u00d2\u00d4\u00da\u00df\u00e6")
        buf.write("\u00ec\u00f7\u0102\3\b\2\2")
        return buf.getvalue()


class MicroCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    IDENTIFIER = 35
    INT_LITERAL = 36
    FLOAT_LITERAL = 37
    STR_LITERAL = 38
    COMMENT = 39
    WS = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'string'", "'='", "'*'", "'int'", "'float'", "'void'", 
            "'('", "')'", "'{'", "'}'", "','", "'read'", "'print'", "'return'", 
            "'if'", "'else'", "'while'", "'-'", "'&'", "'['", "']'", "'malloc'", 
            "'free'", "'<'", "'<='", "'>='", "'=='", "'!='", "'>'", "'/'", 
            "'+'", "'<<'", "'>>'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", "STR_LITERAL", 
            "COMMENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", 
                  "STR_LITERAL", "COMMENT", "WS", "LETTER", "DIGIT" ]

    grammarFileName = "MicroC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
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



