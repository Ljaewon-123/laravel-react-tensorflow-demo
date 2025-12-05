<?php

namespace App\Http\Controllers;

use App\Services\SentimentService;
use Illuminate\Http\Request;
use App\Http\Requests\SentimentRequest;

class SentimentController extends Controller
{
    public function detect(SentimentRequest  $request, SentimentService $service)
    {
        // $validated = $request->validate([
        //     'text' => 'required|string'
        // ]);
        $validated = $request->validated();

        $result = $service->predict($validated['text']);

        return response()->json($result);
    }
}
