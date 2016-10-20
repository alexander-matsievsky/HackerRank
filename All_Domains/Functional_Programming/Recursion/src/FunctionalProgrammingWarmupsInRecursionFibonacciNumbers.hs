{-# LANGUAGE TemplateHaskell #-}
module FunctionalProgrammingWarmupsInRecursionFibonacciNumbers(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All
import           Debug.Trace

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    n = read input
    output = show $ fibonacci !! (n - 1)

fibonacci :: [Integer]
fibonacci = 0:1:zipWith (+) fibonacci (tail fibonacci)

prop_run = run "3" == "1"

return []
runTests = $quickCheckAll
