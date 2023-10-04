<?php

namespace App\Http\Controllers;

use App\Models\Repo;
use Illuminate\Http\Request;

class RepoController extends Controller
{
    public function create(Request $request)
    {
        $readme = '';
        if ($request->get('readme') != '') {
            $readme = $request->get('readme');
        }
        $repo = new Repo([
            'name' => $request->get('name'),
            'readme' => $readme,
            'language' => $request->get('language'),
            'mode' => $request->get('mode'),
            'created_by' => $request->get('user_id'),
        ]);
        $repo->save();
        return response()->json([
            'status' => 200,
            'message' => 'Successfully create repo',
            'data' => $repo
        ]);
    }
    public function index()
    {
        $repos = Repo::all();
        if ($repos) {
            return response()->json([
                'status' => 200,
                'message' => 'Successfully retrieved all repos',
                'data' => $repos
            ]);
        }

        return response()->json([
            'status' => 417,
            'message' => 'No repos existed',
            'data' => [],
        ]);
    }

    public function getRepoById(Request $request)
    {
        $id = $request->get('id');
        $repos = Repo::where('created_by', $id)->get();

        return response()->json([
            'status' => 200,
            'message' => 'Repos found for user with id ' . $id,
            'data' => $repos,
        ]);
    }
}
