{-# LANGUAGE TemplateHaskell #-}
module PascalsTriangle(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All
import           Debug.Trace

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    k = (read::String -> Integer) input
    fact n = product [1..n]
    triangle = [[fact n `div` fact r `div` fact (n - r) | r <- [0..n]] | n <- [0..(k - 1)]]
    output = unlines . map (unwords . map show) $ triangle

prop_run = run "4" == "1\n\
\1 1\n\
\1 2 1\n\
\1 3 3 1\n"

return []
runTests = $quickCheckAll
