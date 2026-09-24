# V2R cluster inventory

2026-09-24T00:03:05.593524+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325579931648 available bytes; 81.84% used; 112500875 free inodes.

server1 `/home`: 325579931648 available bytes; 81.84% used; 112500875 free inodes.

server1 `/tmp`: 325579931648 available bytes; 81.84% used; 112500875 free inodes.

server1 `/var/tmp`: 325579931648 available bytes; 81.84% used; 112500875 free inodes.

server1 `/mnt/raid5`: 1234245234688 available bytes; 94.34% used; 337735355 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41017442304 available bytes; 97.71% used; 110432435 free inodes.

server2 `/home`: 41017442304 available bytes; 97.71% used; 110432435 free inodes.

server2 `/tmp`: 41017442304 available bytes; 97.71% used; 110432435 free inodes.

server2 `/var/tmp`: 41017442304 available bytes; 97.71% used; 110432435 free inodes.

server2 `/mnt/raid5`: 533519020032 available bytes; 96.31% used; 445204128 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292798316544 available bytes; 83.66% used; 114213298 free inodes.

server3 `/home`: 292798316544 available bytes; 83.66% used; 114213298 free inodes.

server3 `/data`: 82266578944 available bytes; 98.86% used; 225844796 free inodes.

server3 `/tmp`: 292798316544 available bytes; 83.66% used; 114213298 free inodes.

server3 `/var/tmp`: 292798316544 available bytes; 83.66% used; 114213298 free inodes.
| server4 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106132267008 available bytes; 94.08% used; 114351167 free inodes.

server4 `/home`: 106132267008 available bytes; 94.08% used; 114351167 free inodes.

server4 `/data`: 292917239808 available bytes; 95.95% used; 225414605 free inodes.

server4 `/tmp`: 106132267008 available bytes; 94.08% used; 114351167 free inodes.

server4 `/var/tmp`: 106132267008 available bytes; 94.08% used; 114351167 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
