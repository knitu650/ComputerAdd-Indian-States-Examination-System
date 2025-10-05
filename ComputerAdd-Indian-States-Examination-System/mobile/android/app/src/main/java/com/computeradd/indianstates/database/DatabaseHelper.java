package com.computeradd.indianstates.database;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import com.computeradd.indianstates.utils.Constants;

public class DatabaseHelper extends SQLiteOpenHelper {
    
    private static final String CREATE_EXAMS_TABLE =
        "CREATE TABLE exams (" +
        "id TEXT PRIMARY KEY, " +
        "title TEXT, " +
        "description TEXT, " +
        "duration INTEGER, " +
        "total_questions INTEGER, " +
        "is_downloaded INTEGER DEFAULT 0)";
    
    private static final String CREATE_QUESTIONS_TABLE =
        "CREATE TABLE questions (" +
        "id TEXT PRIMARY KEY, " +
        "exam_id TEXT, " +
        "question_text TEXT, " +
        "type TEXT, " +
        "options TEXT, " +
        "correct_answer TEXT, " +
        "marks INTEGER, " +
        "FOREIGN KEY(exam_id) REFERENCES exams(id))";
    
    private static final String CREATE_ANSWERS_TABLE =
        "CREATE TABLE answers (" +
        "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
        "question_id TEXT, " +
        "answer TEXT, " +
        "is_synced INTEGER DEFAULT 0, " +
        "timestamp INTEGER)";
    
    public DatabaseHelper(Context context) {
        super(context, Constants.DB_NAME, null, Constants.DB_VERSION);
    }
    
    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(CREATE_EXAMS_TABLE);
        db.execSQL(CREATE_QUESTIONS_TABLE);
        db.execSQL(CREATE_ANSWERS_TABLE);
    }
    
    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS exams");
        db.execSQL("DROP TABLE IF EXISTS questions");
        db.execSQL("DROP TABLE IF EXISTS answers");
        onCreate(db);
    }
}
