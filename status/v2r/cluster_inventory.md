# V2R cluster inventory

2026-09-23T21:19:42.241066+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325720510464 available bytes; 81.83% used; 112501432 free inodes.

server1 `/home`: 325720510464 available bytes; 81.83% used; 112501432 free inodes.

server1 `/tmp`: 325720510464 available bytes; 81.83% used; 112501432 free inodes.

server1 `/var/tmp`: 325720510464 available bytes; 81.83% used; 112501432 free inodes.

server1 `/mnt/raid5`: 1388131782656 available bytes; 93.63% used; 337739962 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 41112162304 available bytes; 97.71% used; 110432692 free inodes.

server2 `/home`: 41112162304 available bytes; 97.71% used; 110432692 free inodes.

server2 `/tmp`: 41112162304 available bytes; 97.71% used; 110432692 free inodes.

server2 `/var/tmp`: 41112162304 available bytes; 97.71% used; 110432692 free inodes.

server2 `/mnt/raid5`: 538846035968 available bytes; 96.28% used; 445209165 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292954259456 available bytes; 83.65% used; 114208570 free inodes.

server3 `/home`: 292954259456 available bytes; 83.65% used; 114208570 free inodes.

server3 `/data`: 52294848512 available bytes; 99.28% used; 225849005 free inodes.

server3 `/tmp`: 292954259456 available bytes; 83.65% used; 114208570 free inodes.

server3 `/var/tmp`: 292954259456 available bytes; 83.65% used; 114208570 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106488037376 available bytes; 94.06% used; 114356025 free inodes.

server4 `/home`: 106488037376 available bytes; 94.06% used; 114356025 free inodes.

server4 `/data`: 300410142720 available bytes; 95.85% used; 225453034 free inodes.

server4 `/tmp`: 106488037376 available bytes; 94.06% used; 114356025 free inodes.

server4 `/var/tmp`: 106488037376 available bytes; 94.06% used; 114356025 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
