import           FunctionalProgrammingWarmupsInRecursionFibonacciNumbers
import           FunctionalProgrammingWarmupsInRecursionGcd
import           FunctionsAndFractalsSierpinskiTriangles
import           PascalsTriangle

main = do
    _ <- FunctionalProgrammingWarmupsInRecursionGcd.runTests
    _ <- FunctionalProgrammingWarmupsInRecursionFibonacciNumbers.runTests
    _ <- PascalsTriangle.runTests
    _ <- FunctionsAndFractalsSierpinskiTriangles.runTests
    return ()
