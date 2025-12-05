<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class SentimentRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        // 인증이나 권한 체크가 필요 없다면 true
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     */
    public function rules(): array
    {
        return [
            'text' => 'required|string',
        ];
    }

    /**
     * Optional: 커스텀 에러 메시지
     */
    public function messages(): array
    {
        return [
            'text.required' => 'text 필드는 필수입니다.',
            'text.string' => 'text는 문자열이어야 합니다.',
        ];
    }
}
