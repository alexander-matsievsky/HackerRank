{-# LANGUAGE TemplateHaskell #-}
module FpHelloWorldNTimes(runTests) where
import           Test.QuickCheck

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    n = read input
    output = unlines . replicate n $ "Hello World"

prop_run = run "4" == "Hello World\n\
\Hello World\n\
\Hello World\n\
\Hello World\n"

return []
runTests = $quickCheckAll
