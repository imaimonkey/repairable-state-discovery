# V2R cluster inventory

2026-09-25T19:38:21.765623+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318726397952 available bytes; 82.22% used; 112476326 free inodes.

server1 `/home`: 318726397952 available bytes; 82.22% used; 112476326 free inodes.

server1 `/tmp`: 318726397952 available bytes; 82.22% used; 112476326 free inodes.

server1 `/var/tmp`: 318726397952 available bytes; 82.22% used; 112476326 free inodes.

server1 `/mnt/raid5`: 370847735808 available bytes; 98.30% used; 337540759 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23102500864 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23102500864 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23102500864 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23102500864 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 311275511808 available bytes; 97.85% used; 445064065 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382597120 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84382597120 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 127198523392 available bytes; 98.24% used; 225808432 free inodes.

server3 `/tmp`: 84382597120 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84382597120 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105674481664 available bytes; 94.10% used; 114349575 free inodes.

server4 `/home`: 105674481664 available bytes; 94.10% used; 114349575 free inodes.

server4 `/data`: 229586964480 available bytes; 96.83% used; 224929717 free inodes.

server4 `/tmp`: 105674481664 available bytes; 94.10% used; 114349575 free inodes.

server4 `/var/tmp`: 105674481664 available bytes; 94.10% used; 114349575 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
