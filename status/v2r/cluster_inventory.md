# V2R cluster inventory

2026-09-26T05:54:55.517857+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318779879424 available bytes; 82.22% used; 112476282 free inodes.

server1 `/home`: 318779879424 available bytes; 82.22% used; 112476282 free inodes.

server1 `/tmp`: 318779879424 available bytes; 82.22% used; 112476282 free inodes.

server1 `/var/tmp`: 318779879424 available bytes; 82.22% used; 112476282 free inodes.

server1 `/mnt/raid5`: 233475121152 available bytes; 98.93% used; 337540008 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22737543168 available bytes; 98.73% used; 110405657 free inodes.

server2 `/home`: 22737543168 available bytes; 98.73% used; 110405657 free inodes.

server2 `/tmp`: 22737543168 available bytes; 98.73% used; 110405657 free inodes.

server2 `/var/tmp`: 22737543168 available bytes; 98.73% used; 110405657 free inodes.

server2 `/mnt/raid5`: 274742181888 available bytes; 98.10% used; 445033763 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82590871552 available bytes; 95.39% used; 114114176 free inodes.

server3 `/home`: 82590871552 available bytes; 95.39% used; 114114176 free inodes.

server3 `/data`: 124016648192 available bytes; 98.29% used; 225823316 free inodes.

server3 `/tmp`: 82590871552 available bytes; 95.39% used; 114114176 free inodes.

server3 `/var/tmp`: 82590871552 available bytes; 95.39% used; 114114176 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106094227456 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094227456 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106988953600 available bytes; 98.52% used; 224929124 free inodes.

server4 `/tmp`: 106094227456 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094227456 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
