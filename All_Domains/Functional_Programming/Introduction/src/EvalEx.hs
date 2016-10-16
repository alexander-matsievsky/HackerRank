{-# LANGUAGE TemplateHaskell #-}
module EvalEx(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All
import           Text.Printf

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    _:xs = map (read::String -> Double) . lines $ input
    output = unlines . map (printf "%.4f". (\x -> sum [x ** i / product [1..i] | i <- [0..9]])) $ xs

prop_run = run "4\n\
\20.0000\n\
\5.0000\n\
\0.5000\n\
\-0.5000\n" == "2423600.1887\n\
\143.6895\n\
\1.6487\n\
\0.6065\n"

return []
runTests = $quickCheckAll
