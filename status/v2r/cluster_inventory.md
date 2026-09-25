# V2R cluster inventory

2026-09-25T13:46:35.817535+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319161298944 available bytes; 82.20% used; 112476970 free inodes.

server1 `/home`: 319161298944 available bytes; 82.20% used; 112476970 free inodes.

server1 `/tmp`: 319161298944 available bytes; 82.20% used; 112476970 free inodes.

server1 `/var/tmp`: 319161298944 available bytes; 82.20% used; 112476970 free inodes.

server1 `/mnt/raid5`: 364133040128 available bytes; 98.33% used; 337547607 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 18781962240 available bytes; 98.95% used; 110408225 free inodes.

server2 `/home`: 18781962240 available bytes; 98.95% used; 110408225 free inodes.

server2 `/tmp`: 18781962240 available bytes; 98.95% used; 110408225 free inodes.

server2 `/var/tmp`: 18781962240 available bytes; 98.95% used; 110408225 free inodes.

server2 `/mnt/raid5`: 322713010176 available bytes; 97.77% used; 445076721 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84281434112 available bytes; 95.30% used; 114154462 free inodes.

server3 `/home`: 84281434112 available bytes; 95.30% used; 114154462 free inodes.

server3 `/data`: 142344048640 available bytes; 98.03% used; 225809438 free inodes.

server3 `/tmp`: 84281434112 available bytes; 95.30% used; 114154462 free inodes.

server3 `/var/tmp`: 84281434112 available bytes; 95.30% used; 114154462 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655513088 available bytes; 94.10% used; 114349714 free inodes.

server4 `/home`: 105655513088 available bytes; 94.10% used; 114349714 free inodes.

server4 `/data`: 231454171136 available bytes; 96.80% used; 224949994 free inodes.

server4 `/tmp`: 105655513088 available bytes; 94.10% used; 114349714 free inodes.

server4 `/var/tmp`: 105655513088 available bytes; 94.10% used; 114349714 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
