import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_vardecl(self):
        input ="""int a, b[6];"""
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',ArrayType(6, IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_decl_in_program(self):
        input ="""int main () {
            getIntLn();
            int a, b[6];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),\
            Block([CallExpr(Id("getIntLn"),[]),VarDecl("a",IntType()),VarDecl("b",ArrayType(6,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_var_fundecl(self):
        input ="""int main () {
            getIntLn();
        }
        int a, b[6];"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),\
            Block([CallExpr(Id("getIntLn"),[])])),VarDecl("a",IntType()),VarDecl("b",ArrayType(6,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_expr_assign(self):
        input ="""int main () {
            a=b=c;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_returnstmt(self):
        input ="""int main () {
            a=b=c;
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c"))),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_blockstmt8(self):
        input ="""int main () {
            a=b=c;
            {

            }
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c"))),Block([]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_blockstmt9(self):
        input ="""int main () {
            a=b=c;
            {
                int b,c;
            }
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),\
            BinaryOp("=",Id("b"),Id("c"))),Block([VarDecl("b",IntType()),VarDecl("c",IntType())]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_parameterdecl10(self):
        input ="""int main (int argv[]) {
            a=b=c;
            {
                int b,c;
            }
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],IntType(),\
            Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c"))),Block([VarDecl("b",IntType()),VarDecl("c",IntType())]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_parameterdecl11(self):
        input ="""int main (int argv[], string argc) {
            a=b=c;
            {
                int b,c;
            }
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType())),VarDecl("argc",StringType())],IntType(),\
            Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c"))),Block([VarDecl("b",IntType()),VarDecl("c",IntType())]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_decl12(self):
        input ="""float b[7];
        int main (int argv[], string argc) {
            a=b=c;
            {
                int b,c;
            }
            return;
        }"""
        expect = str(Program([VarDecl("b",ArrayType(7,FloatType())),FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType())),VarDecl("argc",StringType())],IntType(),\
            Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c"))),Block([VarDecl("b",IntType()),VarDecl("c",IntType())]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_funcdecl13(self):
        input ="""int[] main (int argv[], string argc) {
            a=b=c;
            {
                int b,c;
            }
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType())),VarDecl("argc",StringType())],ArrayPointerType(IntType()),\
            Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c"))),Block([VarDecl("b",IntType()),VarDecl("c",IntType())]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_blockstmt14(self):
        input ="""int[] main (int argv[]) {
            a=b=c;
            {
                int b,c;
                {
                    boolean check;
                }
            }
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),\
            Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c"))),Block([VarDecl("b",IntType()),VarDecl("c",IntType()),Block([VarDecl("check",BoolType())])]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_blockstmt15(self):
        input ="""int[] main (int argv[]) {
            a=b=c;
            {
                
                {
                    boolean check;
                }
                {
                    int b,c;
                }
            }
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),\
            Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c"))),Block([Block([VarDecl("check",BoolType())]),Block([VarDecl("b",IntType()),VarDecl("c",IntType())])]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_voidtype16(self):
        input ="""void main (int argv[]) {
            a=b=c;
            {
                
            }
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),\
            Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c"))),Block([]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_stringtype17(self):
        input ="""void main (int argv[]) {
            a=b=c;
            {
                string d,e,f[8];
            }
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c"))),\
            Block([VarDecl("d",StringType()),VarDecl("e",StringType()),VarDecl("f",ArrayType(8,StringType()))]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_booltype18(self):
        input ="""void main (int argv[]) {
            a=b=c;
            {
                boolean d,e,f[8];
            }
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c"))),\
            Block([VarDecl("d",BoolType()),VarDecl("e",BoolType()),VarDecl("f",ArrayType(8,BoolType()))]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_floattype19(self):
        input ="""void main (int argv[]) {
            a=b=c;
            {
                float d,e,f[8];
            }
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c"))),\
            Block([VarDecl("d",FloatType()),VarDecl("e",FloatType()),VarDecl("f",ArrayType(8,FloatType()))]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_forstmt20(self):
        input ="""void main (int argv[]) {
            for(i =0; i< 7; i=i+1){

            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),\
            BinaryOp("<",Id("i"),IntLiteral(7)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_forstmt21(self):
        input ="""void main (int argv[]) {
            for(i =0; i <= 7; i=i+1){
                int j;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),\
            BinaryOp("<=",Id("i"),IntLiteral(7)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([VarDecl("j",IntType())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_forstmt22(self):
        input ="""void main (int argv[]) {
            for(i =0; i <= 7; i=i+1){
                int j;
                {
                    float k;
                }
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),\
            BinaryOp("<=",Id("i"),IntLiteral(7)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([VarDecl("j",IntType()),Block([VarDecl("k",FloatType())])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_forstmt23(self):
        input ="""void main (int argv[]) {
            for(i =0; i <= 7; i=i+1){
                int j;
                {
                    float k;
                }
                {
                    a+b;
                }
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),\
            Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(7)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),\
                Block([VarDecl("j",IntType()),Block([VarDecl("k",FloatType())]),Block([BinaryOp("+",Id("a"),Id("b"))])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_forstmt24(self):
        input ="""void main (int argv[]) {
            for(i =0; i <= 7; i=i+1){
                for(j = 0; j < n; j = j + 1)
                    i+j;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),\
            Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(7)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),\
                Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("n")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),BinaryOp("+",Id("i"),Id("j")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_forstmt25(self):
        input ="""void main (int argv[]) {
            for(i =0; i <= 7; i=i+1){
                for(j = 0; j < n; j = j + 1)
                    i+j;
                int x, y;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),\
            Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(7)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),\
                Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("n")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),\
                    BinaryOp("+",Id("i"),Id("j"))),VarDecl("x",IntType()),VarDecl("y",IntType())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_forstmt26(self):
        input ="""void main (int argv[]) {
            for(i =0; i <= 7; i=i+1){
                for(j = 0; j < n; j = j + 1)
                    i+j;
                for(k = 0; k < m; k=k+1)
                    k*i;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),\
            Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(7)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),\
                Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("n")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),BinaryOp("+",Id("i"),Id("j"))),\
                    For(BinaryOp("=",Id("k"),IntLiteral(0)),BinaryOp("<",Id("k"),Id("m")),BinaryOp("=",Id("k"),BinaryOp("+",Id("k"),IntLiteral(1))),BinaryOp("*",Id("k"),Id("i")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_forstmt27(self):
        input ="""void main (int argv[]) {
            for(i =0; i <= 7; i=i+1){
                
            }
            for(j = 0; j < n; j= j +1){

            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([For(BinaryOp("=",Id("i"),\
            IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(7)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([])),\
                For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("n")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_forstmt28(self):
        input ="""void main (int argv[]) {
            for(i =0; i <= 7; i=i+1){
                break;
            }
            for(j = 0; j < n; j= j +1){
                continue;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([For(BinaryOp("=",Id("i"),\
            IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(7)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Break()])),\
                For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("n")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([Continue()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_forstmt29(self):
        input ="""void main (int argv[]) {
            for(i =0; i <= 7; i=i+1){
                int a[5],b;
            }
            for(j = 0; j < n; j= j +1){
                float c;
            }
            string d;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),\
            BinaryOp("<=",Id("i"),IntLiteral(7)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([VarDecl("a",ArrayType(5,IntType())),\
                VarDecl("b",IntType())])),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("n")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),\
                    IntLiteral(1))),Block([VarDecl("c",FloatType())])),VarDecl("d",StringType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_ifstmt30(self):
        input ="""void main (int argv[]) {
            if (true){
                a+b;
                c+d;
            }
            else
                x-y;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([If(BooleanLiteral(True),\
            Block([BinaryOp("+",Id("a"),Id("b")),BinaryOp("+",Id("c"),Id("d"))]),BinaryOp("-",Id("x"),Id("y")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_ifstmt31(self):
        input ="""void main (int argv[]) {
            if (true){
                boolean variable[100];
                c+d;
            }
            else
                x-y;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([If(BooleanLiteral(True),\
            Block([VarDecl("variable",ArrayType(100,BoolType())),BinaryOp("+",Id("c"),Id("d"))]),BinaryOp("-",Id("x"),Id("y")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_ifstmt32(self):
        input ="""void main (int argv[]) {
            string str;
            if (true){
                boolean variable[100];
                c+d;
            }
            else
                x-y;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([VarDecl("str",StringType()),If(BooleanLiteral(True),\
            Block([VarDecl("variable",ArrayType(100,BoolType())),BinaryOp("+",Id("c"),Id("d"))]),BinaryOp("-",Id("x"),Id("y")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_ifstmt33(self):
        input ="""void main (int argv[]) {
            string str;
            if (true){
                boolean variable[100];
                c+d;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([VarDecl("str",StringType()),If(BooleanLiteral(True),\
            Block([VarDecl("variable",ArrayType(100,BoolType())),BinaryOp("+",Id("c"),Id("d"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_ifstmt34(self):
        input ="""void main (int argv[]) {
            string str;
            if (true){
                boolean variable[100];
                c+d;
                if (false)
                    return;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([VarDecl("str",StringType()),\
            If(BooleanLiteral(True),Block([VarDecl("variable",ArrayType(100,BoolType())),BinaryOp("+",Id("c"),Id("d")),If(BooleanLiteral(False),Return())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_ifstmt35(self):
        input ="""void main (int argv[]) {
            string str;
            if (true){
                boolean variable[100];
                c+d;
                if (false)
                    return;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([VarDecl("str",StringType()),\
            If(BooleanLiteral(True),Block([VarDecl("variable",ArrayType(100,BoolType())),BinaryOp("+",Id("c"),Id("d")),If(BooleanLiteral(False),Return())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_ifstmt36(self):
        input ="""void main (int argv[]) {
            string str;
            if (true){
                //boolean variable[100];
                c+d;
                if (false)
                    return;
            }
            else if ( false)
                return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),\
            Block([VarDecl("str",StringType()),If(BooleanLiteral(True),Block([BinaryOp("+",Id("c"),Id("d")),If(BooleanLiteral(False),\
                Return())]),If(BooleanLiteral(False),Return()))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_ifstmt37(self):
        input ="""void main (int argv[]) {
            string str;
            if (true){
                //boolean variable[100];
                c+d;
                if (false)
                    return;
            }
            else if ( false)
                return;
            else if (check)
                return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([VarDecl("str",StringType()),\
            If(BooleanLiteral(True),Block([BinaryOp("+",Id("c"),Id("d")),If(BooleanLiteral(False),Return())]),If(BooleanLiteral(False),Return(),\
                If(Id("check"),Return())))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_ifstmt38(self):
        input ="""void main (int argv[]) {
            string str;
            if(hihi)
                check = 1;
            if (true){
                //boolean variable[100];
                c+d;
                if (false)
                    return;
            }
            else if ( false)
                return;
            else if (check)
                return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([VarDecl("str",StringType()),\
            If(Id("hihi"),BinaryOp("=",Id("check"),IntLiteral(1))),If(BooleanLiteral(True),Block([BinaryOp("+",Id("c"),Id("d")),\
                If(BooleanLiteral(False),Return())]),If(BooleanLiteral(False),Return(),If(Id("check"),Return())))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_ifstmt39(self):
        input ="""void main (int argv[]) {
            string str;
            if(hihi)
                check = 1;
            if (true){
                //boolean variable[100];
                c+d;
                if (false)
                    return;
                else
                    check;
            }
            else if ( false)
                return;
            else if (check)
                return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([VarDecl("str",StringType()),\
            If(Id("hihi"),BinaryOp("=",Id("check"),IntLiteral(1))),If(BooleanLiteral(True),Block([BinaryOp("+",Id("c"),Id("d")),If(BooleanLiteral(False),\
                Return(),Id("check"))]),If(BooleanLiteral(False),Return(),If(Id("check"),Return())))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_whilestmt40(self):
        input ="""void main (int argv[]) {
            do{
                i = i + 1;
            }while ( argv[i]);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([Dowhile([\
            Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],ArrayCell(Id("argv"),Id("i")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_whilestmt41(self):
        input ="""void main (int argv[]) {
            do{
                i = i + 1;
                float b[9], c;
            }while ( argv[i]);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([Dowhile([\
            Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),VarDecl("b",ArrayType(9,FloatType())),VarDecl("c",FloatType())])],ArrayCell(Id("argv"),Id("i")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_whilestmt42(self):
        input ="""void main (int argv[]) {
            do{
                i = i + 1;
                float b[9], c;
            }while ( argv[i]);
            do{
                i = i + 1;
            }
            {
                j = j + 1;
            }while(forfun);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([Dowhile([\
            Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),VarDecl("b",ArrayType(9,FloatType())),VarDecl("c",FloatType())])],\
                ArrayCell(Id("argv"),Id("i"))),Dowhile([Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]),\
                    Block([BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1)))])],Id("forfun"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_whilestmt43(self):
        input ="""void main (int argv[]) {
            string char;
            do{
                i = i + 1;
            }
            {
                j = j + 1;
            }while(forfun);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([\
            VarDecl("char",StringType()),Dowhile([Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]),\
                Block([BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1)))])],Id("forfun"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_whilestmt44(self):
        input ="""void main (int argv[]) {
            do{
                do{
                    i = i + 1;
                }while(true);
            }while(false);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([\
            Dowhile([Block([Dowhile([Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],\
                BooleanLiteral(True))])],BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_whilestmt45(self):
        input ="""void main (int argv[]) {
            do{
                do{
                    i = i + 1;
                }while(1);
                do{
                    j = j + 1;
                }while(2);
            }while(0);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([\
            Dowhile([Block([Dowhile([Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],\
                IntLiteral(1)),Dowhile([Block([BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1)))])],IntLiteral(2))])],IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_whilestmt46(self):
        input ="""void main (int argv[]) {
            do{
                do{
                    i = i + 1;
                    do{
                    j = j + 1;
                    }while(2);
                }while(1);
            }while(0);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([Dowhile([Block([Dowhile([Block([\
            BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Dowhile([Block([BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1)))])],\
                IntLiteral(2))])],IntLiteral(1))])],IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_whilestmt47(self):
        input ="""void main (int argv[]) {
            do{
                do{

                }
                while(1);
            }while(2);
            do{

            }while(3);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([Dowhile([\
            Block([Dowhile([Block([])],IntLiteral(1))])],IntLiteral(2)),Dowhile([Block([])],IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_whilestmt48(self):
        input ="""void main (int argv[]) {
            do{
                do{

                }
                while(1);
            }while(2);
            do{
                do{

                }while(4);
            }while(3);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([Dowhile([Block([\
            Dowhile([Block([])],IntLiteral(1))])],IntLiteral(2)),Dowhile([Block([Dowhile([Block([])],IntLiteral(4))])],IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_whilestmt49(self):
        input ="""void main (int argv[]) {
            do{
                do{
                    do{
                        do{

                        }while(4);
                    }while(3);
                }
                while(1);
            }while(2);
            
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([\
            Dowhile([Block([Dowhile([Block([Dowhile([Block([Dowhile([Block([])],IntLiteral(4))])],IntLiteral(3))])],IntLiteral(1))])],IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_funcdecl50(self):
        input ="""void main (int argv[]) {
            return;
            
        }
        boolean isPrime(float n){
            return false;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),\
            Block([Return()])),FuncDecl(Id("isPrime"),[VarDecl("n",FloatType())],BoolType(),Block([Return(BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_funcdecl51(self):
        input ="""void main (int argv[]) {
            return;
            
        }
        boolean isPrime(float n){
            return false;
        }
        string[] concate(string a[], string b[]){
            return a+b;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argv",ArrayPointerType(IntType()))],VoidType(),Block([Return()])),\
            FuncDecl(Id("isPrime"),[VarDecl("n",FloatType())],BoolType(),Block([Return(BooleanLiteral(False))])),\
                FuncDecl(Id("concate"),[VarDecl("a",ArrayPointerType(StringType())),VarDecl("b",ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([Return(BinaryOp("+",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_funcdecl52(self):
        input ="""void main () {
            return;
            
        }
        boolean isPrime(){
            return false;
        }
        string[] concate(){
            return a+b;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return()])),FuncDecl(Id("isPrime"),[],\
            BoolType(),Block([Return(BooleanLiteral(False))])),FuncDecl(Id("concate"),[],ArrayPointerType(StringType()),Block([Return(BinaryOp("+",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_decl53(self):
        input ="""void main () {
            return;
            
        }
        boolean isPrime(){
            return false;
        }
        float maximum;
        float minimum, average[2];
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return()])),FuncDecl(Id("isPrime"),[],BoolType(),\
            Block([Return(BooleanLiteral(False))])),VarDecl("maximum",FloatType()),VarDecl("minimum",FloatType()),VarDecl("average",ArrayType(2,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_decl54(self):
        input ="""void main () {
            int term;
            return;
        }
        boolean isPrime(){
            return false;
            string chr;
        }
        float maximum;
        float minimum, average[2];
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("term",IntType()),Return()])),FuncDecl(Id("isPrime"),[],\
            BoolType(),Block([Return(BooleanLiteral(False)),VarDecl("chr",StringType())])),VarDecl("maximum",FloatType()),\
                VarDecl("minimum",FloatType()),VarDecl("average",ArrayType(2,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_decl55(self):
        input ="""void main () {
            int term;
            return;
        }
        boolean isPrime(){
            return false;
            string chr;
            {
                boolean check;
            }
        }
        float maximum;
        float minimum, average[2];
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("term",IntType()),Return()])),FuncDecl(Id("isPrime"),[],\
            BoolType(),Block([Return(BooleanLiteral(False)),VarDecl("chr",StringType()),Block([VarDecl("check",BoolType())])])),\
                VarDecl("maximum",FloatType()),VarDecl("minimum",FloatType()),VarDecl("average",ArrayType(2,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_decl56(self):
        input ="""void main () {
            int term;
            return;
        }
        boolean isPrime(){
            {
                boolean check;
                {
                    string chr;
                }
            }
        }
        float maximum;
        float minimum, average[2];
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("term",IntType()),Return()])),\
            FuncDecl(Id("isPrime"),[],BoolType(),Block([Block([VarDecl("check",BoolType()),Block([VarDecl("chr",StringType())])])])),\
                VarDecl("maximum",FloatType()),VarDecl("minimum",FloatType()),VarDecl("average",ArrayType(2,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_decl57(self):
        input ="""void main () {
            int term;
            if (a> b){
                boolean c;
            }
            return;
        }
        float minimum, average[2];
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("term",IntType()),If(BinaryOp(">",Id("a"),Id("b")),\
            Block([VarDecl("c",BoolType())])),Return()])),VarDecl("minimum",FloatType()),VarDecl("average",ArrayType(2,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_decl58(self):
        input ="""void main () {
            int term;
            for(i;j;k){
                string b[8];
            }
            return;
        }
        float minimum, average[2];
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("term",IntType()),For(Id("i"),Id("j"),Id("k"),\
            Block([VarDecl("b",ArrayType(8,StringType()))])),Return()])),VarDecl("minimum",FloatType()),VarDecl("average",ArrayType(2,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_decl59(self):
        input ="""void main () {
            int term;
            do{
                int somesome;
            }while( a <n);
            return;
        }
        float minimum, average[2];
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("term",IntType()),Dowhile([\
            Block([VarDecl("somesome",IntType())])],BinaryOp("<",Id("a"),Id("n"))),Return()])),VarDecl("minimum",FloatType()),VarDecl("average",ArrayType(2,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_expr60(self):
        input ="""void main () {
            a = b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_expr61(self):
        input ="""void main () {
            a = b = c;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_expr62(self):
        input ="""void main () {
            a || b || c;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("||",BinaryOp("||",Id("a"),Id("b")),Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_expr63(self):
        input ="""void main () {
            a && b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("&&",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_expr64(self):
        input ="""void main () {
            a && b && c;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("&&",BinaryOp("&&",Id("a"),Id("b")),Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_expr65(self):
        input ="""void main () {
            a == b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("==",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_expr66(self):
        input ="""void main () {
            a != b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("!=",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_expr67(self):
        input ="""void main () {
            a < b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("<",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_expr68(self):
        input ="""void main () {
            a <= b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("<=",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_expr69(self):
        input ="""void main () {
            a > b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp(">",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_expr70(self):
        input ="""void main () {
            a >= b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp(">=",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_expr71(self):
        input ="""void main () {
            a + b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("+",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_expr72(self):
        input ="""void main () {
            a + b + c;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_expr73(self):
        input ="""void main () {
            a - b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("-",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_expr74(self):
        input ="""void main () {
            a - b - c;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("-",BinaryOp("-",Id("a"),Id("b")),Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_expr75(self):
        input ="""void main () {
            a / b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("/",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_expr76(self):
        input ="""void main () {
            a * b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_expr77(self):
        input ="""void main () {
            a % b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("%",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_expr78(self):
        input ="""void main () {
            a % b % c;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("%",BinaryOp("%",Id("a"),Id("b")),Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_expr79(self):
        input ="""void main () {
            a * b * c;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",BinaryOp("*",Id("a"),Id("b")),Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_expr80(self):
        input ="""void main () {
            a / b / c;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("/",BinaryOp("/",Id("a"),Id("b")),Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_expr81(self):
        input ="""void main () {
            -a;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([UnaryOp("-",Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_expr82(self):
        input ="""void main () {
            !a;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([UnaryOp("!",Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_expr83(self):
        input ="""void main () {
            ---a;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([UnaryOp("-",UnaryOp("-",UnaryOp("-",Id("a"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_expr84(self):
        input ="""void main () {
            !!!a;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("a"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_expr85(self):
        input ="""void main () {
            a[b];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([ArrayCell(Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_expr86(self):
        input ="""void main () {
            a[7 + 8];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([ArrayCell(Id("a"),BinaryOp("+",IntLiteral(7),IntLiteral(8)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_expr87(self):
        input ="""void main () {
            a[6.7];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([ArrayCell(Id("a"),FloatLiteral(6.7))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_expr88(self):
        input ="""void main () {
            a = (b + c);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("b"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_expr89(self):
        input ="""void main () {
            a = (b + c)/100;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("+",Id("b"),Id("c")),IntLiteral(100)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_expr90(self):
        input ="""void main () {
            a = (b + c)/100;
            return (aj*fact(aj-1));
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("+",Id("b"),Id("c")),IntLiteral(100))),\
            Return(BinaryOp("*",Id("aj"),CallExpr(Id("fact"),[BinaryOp("-",Id("aj"),IntLiteral(1))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_expr91(self):
        input ="""void main () {
            1.2e1 + e - 6.e-3 && .09e-8;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("&&",BinaryOp("-",BinaryOp("+",FloatLiteral(12.0),Id("e")),\
            FloatLiteral(0.006)),FloatLiteral(9e-10))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_expr92(self):
        input ="""void main () {
            x = a + (b = f()) + (c = g()) * 7;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("x"),BinaryOp("+",BinaryOp("+",Id("a"),\
            BinaryOp("=",Id("b"),CallExpr(Id("f"),[]))),BinaryOp("*",BinaryOp("=",Id("c"),CallExpr(Id("g"),[])),IntLiteral(7))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_expr93(self):
        input ="""void main () {
            foo(2)[3+x] = a[b[2]] + 3;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),\
            BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_expr94(self):
        input ="""void main () {
            return putIntLn(4);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return(CallExpr(Id("putIntLn"),[IntLiteral(4)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_expr95(self):
        input ="""void main () {
            return (foo[2])[3];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return(ArrayCell(ArrayCell(Id("foo"),IntLiteral(2)),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_expr96(self):
        input ="""void main () {
            x=a && b == c;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("x"),BinaryOp("&&",Id("a"),BinaryOp("==",Id("b"),Id("c"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_expr97(self):
        input ="""void main () {
            a= b > c = d = g != f[7] * y;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("=",BinaryOp(">",Id("b"),Id("c")),\
            BinaryOp("=",Id("d"),BinaryOp("!=",Id("g"),BinaryOp("*",ArrayCell(Id("f"),IntLiteral(7)),Id("y"))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_expr98(self):
        input ="""void main () {
            a+c= (3 < 4) + (6 == 64 / 4);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",BinaryOp("+",Id("a"),Id("c")),BinaryOp("+",BinaryOp("<",IntLiteral(3),IntLiteral(4)),\
            BinaryOp("==",IntLiteral(6),BinaryOp("/",IntLiteral(64),IntLiteral(4)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_expr99(self):
        input ="""void main () {
            a= b != (c [0] + d)*a;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("!=",Id("b"),\
            BinaryOp("*",BinaryOp("+",ArrayCell(Id("c"),IntLiteral(0)),Id("d")),Id("a"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))