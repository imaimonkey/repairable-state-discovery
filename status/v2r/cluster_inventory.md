# V2R cluster inventory

2026-09-24T01:06:32.314165+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325523193856 available bytes; 81.84% used; 112500192 free inodes.

server1 `/home`: 325523193856 available bytes; 81.84% used; 112500192 free inodes.

server1 `/tmp`: 325523193856 available bytes; 81.84% used; 112500192 free inodes.

server1 `/var/tmp`: 325523193856 available bytes; 81.84% used; 112500192 free inodes.

server1 `/mnt/raid5`: 993264091136 available bytes; 95.44% used; 337734850 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40967499776 available bytes; 97.71% used; 110432180 free inodes.

server2 `/home`: 40967499776 available bytes; 97.71% used; 110432180 free inodes.

server2 `/tmp`: 40967499776 available bytes; 97.71% used; 110432180 free inodes.

server2 `/var/tmp`: 40967499776 available bytes; 97.71% used; 110432180 free inodes.

server2 `/mnt/raid5`: 531116417024 available bytes; 96.33% used; 445202082 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292383977472 available bytes; 83.68% used; 114189016 free inodes.

server3 `/home`: 292383977472 available bytes; 83.68% used; 114189016 free inodes.

server3 `/data`: 82087424000 available bytes; 98.87% used; 225843131 free inodes.

server3 `/tmp`: 292383977472 available bytes; 83.68% used; 114189016 free inodes.

server3 `/var/tmp`: 292383977472 available bytes; 83.68% used; 114189016 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106009657344 available bytes; 94.08% used; 114349377 free inodes.

server4 `/home`: 106009657344 available bytes; 94.08% used; 114349377 free inodes.

server4 `/data`: 292725022720 available bytes; 95.95% used; 225405418 free inodes.

server4 `/tmp`: 106009657344 available bytes; 94.08% used; 114349377 free inodes.

server4 `/var/tmp`: 106009657344 available bytes; 94.08% used; 114349377 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
