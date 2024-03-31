from . import db_session
from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify
from .jobs import Jobs
from .reqparse import parser


def abort_if_jobs_not_found(job_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(job_id)
    if not jobs:
        abort(404, message=f"Jobs {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_jobs_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        return jsonify(
            {'users': jobs.to_dict(
                only=('job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader'))})

    def delete(self, job_id):
        abort_if_jobs_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader')) for item
                                 in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args['start_date'],
            end_date=args['end_date'],
            is_finished=args['is_finished'],
            team_leader=args['team_leader']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'id': jobs.id})
