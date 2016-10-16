{-# LANGUAGE TemplateHaskell #-}
module FpSolveMeFirst(runTests) where
import Test.QuickCheck
import Test.QuickCheck.All

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    a:b:_ = map (read::String -> Integer) . lines $ input
    output = show $ a + b

prop_run = run "2\n\
\3\n" == "5"

return []
runTests = $quickCheckAll
