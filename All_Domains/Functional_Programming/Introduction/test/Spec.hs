{-# LANGUAGE RankNTypes #-}

import           FpSolveMeFirst

main :: IO ()
main = do
    _ <- FpSolveMeFirst.runTests
    return ()
