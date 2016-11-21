{-# LANGUAGE LambdaCase      #-}
{-# LANGUAGE TemplateHaskell #-}
module ConvexHullFp(runTests) where
import           Data.List
import           Debug.Trace
import           Test.QuickCheck

main :: IO ()
main = interact run

run :: String -> String
run input = trace output output where
    output = show $ perimeter . convexHull $ points
    points = [let x::Int; y::Int
                  x:y:_ = map read . words $ line
              in  (x, y) | line <- drop 1 . lines $ input]

perimeter :: [(Int, Int)] -> Float
perimeter points = sum [distance p1 p2 | (p1, p2) <- segments] where
    distance (x1, y1) (x2, y2) = sqrt . fromIntegral $ (x1 - x2) ^ 2 + (y1 - y2) ^ 2
    segments = zip points (drop 1 . cycle $ points)

convexHull :: [(Int, Int)] -> [(Int, Int)]
convexHull points = tail lowerHull ++ tail upperHull where
    lowerHull = foldl step [] sortedPoints
    upperHull = foldl step [] (reverse sortedPoints)
    step hull p = case hull of
        p2:p1:hull' | clockwiseTurn p1 p2 p -> step (p1:hull') p
        _           -> p:hull
    clockwiseTurn (x1, y1) (x2, y2) (x0, y0) = cross <= 0 where
        cross = (x2 - x1) * (y0 - y1) - (y2 - y1) * (x0 - x1)
    sortedPoints = sort points

prop_run = (run . unlines $ [
    "6",
    "1 1",
    "2 5",
    "3 3",
    "5 3",
    "3 2",
    "2 2"]) == "12.200792"

return []
runTests = $quickCheckAll
