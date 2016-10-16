import           FpHelloWorld
import           FpSolveMeFirst

main = do
    _ <- FpSolveMeFirst.runTests
    _ <- FpHelloWorld.runTests
    return ()