# V2R cluster inventory

2026-09-25T18:37:11.733996+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318747242496 available bytes; 82.22% used; 112476344 free inodes.

server1 `/home`: 318747242496 available bytes; 82.22% used; 112476344 free inodes.

server1 `/tmp`: 318747242496 available bytes; 82.22% used; 112476344 free inodes.

server1 `/var/tmp`: 318747242496 available bytes; 82.22% used; 112476344 free inodes.

server1 `/mnt/raid5`: 371173806080 available bytes; 98.30% used; 337541624 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23102234624 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23102234624 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23102234624 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23102234624 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 313765064704 available bytes; 97.83% used; 445066460 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382269440 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84382269440 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 131385753600 available bytes; 98.18% used; 225809638 free inodes.

server3 `/tmp`: 84382269440 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84382269440 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105607311360 available bytes; 94.11% used; 114349600 free inodes.

server4 `/home`: 105607311360 available bytes; 94.11% used; 114349600 free inodes.

server4 `/data`: 229694582784 available bytes; 96.83% used; 224931665 free inodes.

server4 `/tmp`: 105607311360 available bytes; 94.11% used; 114349600 free inodes.

server4 `/var/tmp`: 105607311360 available bytes; 94.11% used; 114349600 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
