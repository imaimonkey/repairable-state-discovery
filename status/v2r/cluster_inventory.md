# V2R cluster inventory

2026-09-26T04:40:52.289975+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318398861312 available bytes; 82.24% used; 112476278 free inodes.

server1 `/home`: 318398861312 available bytes; 82.24% used; 112476278 free inodes.

server1 `/tmp`: 318398861312 available bytes; 82.24% used; 112476278 free inodes.

server1 `/var/tmp`: 318398861312 available bytes; 82.24% used; 112476278 free inodes.

server1 `/mnt/raid5`: 330493788160 available bytes; 98.48% used; 337545404 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22929387520 available bytes; 98.72% used; 110406198 free inodes.

server2 `/home`: 22929387520 available bytes; 98.72% used; 110406198 free inodes.

server2 `/tmp`: 22929387520 available bytes; 98.72% used; 110406198 free inodes.

server2 `/var/tmp`: 22929387520 available bytes; 98.72% used; 110406198 free inodes.

server2 `/mnt/raid5`: 285182574592 available bytes; 98.03% used; 445050307 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84527599616 available bytes; 95.28% used; 114174590 free inodes.

server3 `/home`: 84527599616 available bytes; 95.28% used; 114174590 free inodes.

server3 `/data`: 124395327488 available bytes; 98.28% used; 225817570 free inodes.

server3 `/tmp`: 84527599616 available bytes; 95.28% used; 114174590 free inodes.

server3 `/var/tmp`: 84527599616 available bytes; 95.28% used; 114174590 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106002112512 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106002112512 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 107068534784 available bytes; 98.52% used; 224929357 free inodes.

server4 `/tmp`: 106002112512 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106002112512 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
