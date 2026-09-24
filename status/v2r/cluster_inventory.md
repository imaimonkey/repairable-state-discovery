# V2R cluster inventory

2026-09-24T00:29:23.832731+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325548990464 available bytes; 81.84% used; 112500601 free inodes.

server1 `/home`: 325548990464 available bytes; 81.84% used; 112500601 free inodes.

server1 `/tmp`: 325548990464 available bytes; 81.84% used; 112500601 free inodes.

server1 `/var/tmp`: 325548990464 available bytes; 81.84% used; 112500601 free inodes.

server1 `/mnt/raid5`: 1146689548288 available bytes; 94.74% used; 337735150 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40995987456 available bytes; 97.71% used; 110432341 free inodes.

server2 `/home`: 40995987456 available bytes; 97.71% used; 110432341 free inodes.

server2 `/tmp`: 40995987456 available bytes; 97.71% used; 110432341 free inodes.

server2 `/var/tmp`: 40995987456 available bytes; 97.71% used; 110432341 free inodes.

server2 `/mnt/raid5`: 532830367744 available bytes; 96.32% used; 445203595 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 291889205248 available bytes; 83.71% used; 114172889 free inodes.

server3 `/home`: 291889205248 available bytes; 83.71% used; 114172889 free inodes.

server3 `/data`: 82239348736 available bytes; 98.86% used; 225844248 free inodes.

server3 `/tmp`: 291889205248 available bytes; 83.71% used; 114172889 free inodes.

server3 `/var/tmp`: 291889205248 available bytes; 83.71% used; 114172889 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106080980992 available bytes; 94.08% used; 114350363 free inodes.

server4 `/home`: 106080980992 available bytes; 94.08% used; 114350363 free inodes.

server4 `/data`: 292921049088 available bytes; 95.95% used; 225414579 free inodes.

server4 `/tmp`: 106080980992 available bytes; 94.08% used; 114350363 free inodes.

server4 `/var/tmp`: 106080980992 available bytes; 94.08% used; 114350363 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
