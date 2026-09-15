from __future__ import annotations

from repairable_diffusion.src.analysis.evaluate import evaluate_repair_selection
from repairable_diffusion.src.analysis.predictor import fit_crossfit_predictor_scores


def test_crossfit_scores_never_use_full_fit_for_supervised_items() -> None:
    train_rows = [
        {"item_id": 1, "trajectory_id": 0, "step_index": 1, "x": 0.0, "label": 0},
        {"item_id": 1, "trajectory_id": 0, "step_index": 2, "x": 1.0, "label": 1},
        {"item_id": 2, "trajectory_id": 0, "step_index": 1, "x": 0.1, "label": 0},
        {"item_id": 2, "trajectory_id": 0, "step_index": 2, "x": 1.1, "label": 1},
    ]
    inference_rows = [dict(row) for row in train_rows]
    inference_rows.append(
        {"item_id": 3, "trajectory_id": 0, "step_index": 1, "x": 0.5}
    )

    scores, metrics, _ = fit_crossfit_predictor_scores(
        train_rows,
        inference_rows,
        ["x"],
        requested_folds=2,
        random_state=7,
        max_iter=100,
    )

    supervised = [row for row in scores if row["item_id"] in {1, 2}]
    unseen = [row for row in scores if row["item_id"] == 3]
    assert supervised
    assert all(row["score_source"] == "crossfit_oof" for row in supervised)
    assert all(row["crossfit_fold"] in {0, 1} for row in supervised)
    assert unseen[0]["score_source"] == "full_fit_unseen_item"
    assert metrics["evaluation_protocol"] == "item_grouped_crossfit_oof"
    assert metrics["crossfit_folds"] == 2


def test_net_policy_metric_counts_damage_to_originally_correct_items(tmp_path) -> None:
    trajectories = {
        "records": [
            {
                "item_id": 1,
                "trajectory_id": 0,
                "correct": True,
            },
            {
                "item_id": 2,
                "trajectory_id": 0,
                "correct": False,
            },
        ]
    }
    oracle = {
        "meta": {
            "branch_count": 1,
            "failed_trajectories": 1,
            "successful_trajectories": 1,
            "negative_repair_measured": True,
        },
        "results": [
            {
                "item_id": 2,
                "trajectory_id": 0,
                "step_results": [
                    {
                        "step_index": 1,
                        "state_token_conf_mean": 0.1,
                        "correction_rate": 1.0,
                    }
                ],
            }
        ],
        "success_results": [
            {
                "item_id": 1,
                "trajectory_id": 0,
                "step_results": [
                    {
                        "step_index": 1,
                        "state_token_conf_mean": 0.1,
                        "degradation_rate": 1.0,
                    }
                ],
            }
        ],
    }
    cfg = {
        "predictor": {"random_state": 7},
        "evaluation": {"selectors": ["confidence"]},
    }

    payload = evaluate_repair_selection(cfg, tmp_path, trajectories, oracle, None)
    row = payload["selectors"][0]

    assert row["net_metric_complete"] is True
    assert row["base_item_pass_at_k"] == 0.5
    assert row["expected_repaired_item_pass_at_k"] == 1.0
    assert row["net_expected_item_pass_at_k"] == 0.5
    assert row["net_policy_gain_over_base_pass_at_k"] == 0.0
    assert row["expected_lost_solved_items"] == 1.0
