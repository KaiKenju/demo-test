<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;

class UserController extends Controller
{
    public function index()
    {
        $users = User::all();

        return response()->json([
            'status' => 200,
            'message' => 'Successfully retrieved all users',
            'data' => $users
        ]);
    }
}
