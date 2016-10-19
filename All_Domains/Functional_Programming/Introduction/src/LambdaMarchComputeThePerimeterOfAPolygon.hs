{-# LANGUAGE TemplateHaskell #-}
module LambdaMarchComputeThePerimeterOfAPolygon(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All
import           Debug.Trace

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    lines' = drop 1 . map (map (read::String -> Float) . words) . lines $ input
    segments = zip lines' (tail . cycle $ lines')
    perimeter = sum [sqrt ((x2 - x1) ** 2 + (y2 - y1) ** 2) | ([x1, y1], [x2, y2]) <- segments]
    output = show perimeter

prop_run = run "4\n\
\0 0\n\
\0 1\n\
\1 1\n\
\1 0\n" == "4.0"

return []
runTests = $quickCheckAll
