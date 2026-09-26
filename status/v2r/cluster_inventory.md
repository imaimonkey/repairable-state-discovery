# V2R cluster inventory

2026-09-26T04:14:07.385132+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318410432512 available bytes; 82.24% used; 112476271 free inodes.

server1 `/home`: 318410432512 available bytes; 82.24% used; 112476271 free inodes.

server1 `/tmp`: 318410432512 available bytes; 82.24% used; 112476271 free inodes.

server1 `/var/tmp`: 318410432512 available bytes; 82.24% used; 112476271 free inodes.

server1 `/mnt/raid5`: 330551623680 available bytes; 98.48% used; 337545539 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22937346048 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22937346048 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22937346048 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22937346048 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 285955039232 available bytes; 98.02% used; 445051087 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84145086464 available bytes; 95.30% used; 114148304 free inodes.

server3 `/home`: 84145086464 available bytes; 95.30% used; 114148304 free inodes.

server3 `/data`: 124586987520 available bytes; 98.28% used; 225819786 free inodes.

server3 `/tmp`: 84145086464 available bytes; 95.30% used; 114148304 free inodes.

server3 `/var/tmp`: 84145086464 available bytes; 95.30% used; 114148304 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106002898944 available bytes; 94.08% used; 114348208 free inodes.

server4 `/home`: 106002898944 available bytes; 94.08% used; 114348208 free inodes.

server4 `/data`: 109670985728 available bytes; 98.48% used; 224929427 free inodes.

server4 `/tmp`: 106002898944 available bytes; 94.08% used; 114348208 free inodes.

server4 `/var/tmp`: 106002898944 available bytes; 94.08% used; 114348208 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
