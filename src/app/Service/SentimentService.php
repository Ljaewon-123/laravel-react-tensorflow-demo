<?php

namespace App\Services;

use Illuminate\Support\Facades\Http;
use App/DTO/SentimentResult;

class SentimentService
{
    public function predict(string $text): SentimentResult
    {
        $response = Http::post("http://ai_inference:8000/predict", [
            "text" => $text,
        ]);

        return SentimentResult::fromArray($response->json());
    }
}
