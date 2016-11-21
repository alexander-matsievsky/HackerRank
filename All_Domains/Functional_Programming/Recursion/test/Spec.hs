import           ConvexHullFp
import           FunctionalProgrammingWarmupsInRecursionFibonacciNumbers
import           FunctionalProgrammingWarmupsInRecursionGcd
import           FunctionsAndFractalsSierpinskiTriangles
import           PascalsTriangle
import           StringCompression
import           StringMingling
import           StringOPermute

main = do
    _ <- FunctionalProgrammingWarmupsInRecursionGcd.runTests
    _ <- FunctionalProgrammingWarmupsInRecursionFibonacciNumbers.runTests
    _ <- PascalsTriangle.runTests
    _ <- FunctionsAndFractalsSierpinskiTriangles.runTests
    _ <- StringMingling.runTests
    _ <- StringOPermute.runTests
    _ <- ConvexHullFp.runTests
    _ <- StringCompression.runTests
    return ()
