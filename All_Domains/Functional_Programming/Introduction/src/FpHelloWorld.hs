{-# LANGUAGE TemplateHaskell #-}
module FpHelloWorld(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    output = "Hello World"

prop_run = run "" == "Hello World"

return []
runTests = $quickCheckAll
