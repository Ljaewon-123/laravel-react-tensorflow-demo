<?php

namespace App\DTO;

class SentimentResult
{
    public function __construct(
        public string $sentiment,
        public float $score
    ) {}

    public static function fromArray(array $data): self
    {
        return new self(
            sentiment: $data['sentiment'],
            score: $data['score'],
        );
    }
}
