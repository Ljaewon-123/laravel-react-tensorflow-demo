<?php

namespace App\Http\Controllers;

use App\Services\SentimentService;
use Illuminate\Http\Request;
use App\Http\Requests\SentimentRequest;
use Illuminate\Support\Facades\Log;

class SentimentController extends Controller
{
    public function detect(SentimentRequest  $request, SentimentService $service)
    {
        // $validated = $request->validate([
        //     'text' => 'required|string'
        // ]);
        $validated = $request->validated();

        $result = $service->predict($validated['text']);

        Log::info('sentiment request', $validated);
        Log::info('sentiment result', $result);

        return response()->json($result);
    }
}
