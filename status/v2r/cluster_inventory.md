# V2R cluster inventory

2026-09-26T09:17:35.062311+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318736957440 available bytes; 82.22% used; 112475800 free inodes.

server1 `/home`: 318736957440 available bytes; 82.22% used; 112475800 free inodes.

server1 `/tmp`: 318736957440 available bytes; 82.22% used; 112475800 free inodes.

server1 `/var/tmp`: 318736957440 available bytes; 82.22% used; 112475800 free inodes.

server1 `/mnt/raid5`: 218999914496 available bytes; 99.00% used; 337538720 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22325100544 available bytes; 98.75% used; 110403915 free inodes.

server2 `/home`: 22325100544 available bytes; 98.75% used; 110403915 free inodes.

server2 `/tmp`: 22325100544 available bytes; 98.75% used; 110403915 free inodes.

server2 `/var/tmp`: 22325100544 available bytes; 98.75% used; 110403915 free inodes.

server2 `/mnt/raid5`: 254576431104 available bytes; 98.24% used; 445023571 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82661023744 available bytes; 95.39% used; 114110817 free inodes.

server3 `/home`: 82661023744 available bytes; 95.39% used; 114110817 free inodes.

server3 `/data`: 123660754944 available bytes; 98.29% used; 225828041 free inodes.

server3 `/tmp`: 82661023744 available bytes; 95.39% used; 114110817 free inodes.

server3 `/var/tmp`: 82661023744 available bytes; 95.39% used; 114110817 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106045923328 available bytes; 94.08% used; 114348132 free inodes.

server4 `/home`: 106045923328 available bytes; 94.08% used; 114348132 free inodes.

server4 `/data`: 89327996928 available bytes; 98.77% used; 224883320 free inodes.

server4 `/tmp`: 106045923328 available bytes; 94.08% used; 114348132 free inodes.

server4 `/var/tmp`: 106045923328 available bytes; 94.08% used; 114348132 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
