import           FunctionalProgrammingWarmupsInRecursionFibonacciNumbers
import           FunctionalProgrammingWarmupsInRecursionGcd
import           FunctionsAndFractalsSierpinskiTriangles
import           PascalsTriangle
import           StringMingling

main = do
    _ <- FunctionalProgrammingWarmupsInRecursionGcd.runTests
    _ <- FunctionalProgrammingWarmupsInRecursionFibonacciNumbers.runTests
    _ <- PascalsTriangle.runTests
    _ <- FunctionsAndFractalsSierpinskiTriangles.runTests
    _ <- StringMingling.runTests
    return ()
