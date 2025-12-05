<?php

namespace App\Http\Controllers;

use App\Services\SentimentService;
use Illuminate\Http\Request;

class SentimentController extends Controller
{
    public function detect(Request $request, SentimentService $service)
    {
        $validated = $request->validate([
            'text' => 'required|string'
        ]);

        $result = $service->predict($validated['text']);

        return response()->json($result);
    }
}
