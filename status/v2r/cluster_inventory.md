# V2R cluster inventory

2026-09-25T14:27:48.721362+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319159250944 available bytes; 82.20% used; 112476978 free inodes.

server1 `/home`: 319159250944 available bytes; 82.20% used; 112476978 free inodes.

server1 `/tmp`: 319159250944 available bytes; 82.20% used; 112476978 free inodes.

server1 `/var/tmp`: 319159250944 available bytes; 82.20% used; 112476978 free inodes.

server1 `/mnt/raid5`: 367451897856 available bytes; 98.31% used; 337547408 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 7394336768 available bytes; 99.59% used; 110407602 free inodes.

server2 `/home`: 7394336768 available bytes; 99.59% used; 110407602 free inodes.

server2 `/tmp`: 7394336768 available bytes; 99.59% used; 110407602 free inodes.

server2 `/var/tmp`: 7394336768 available bytes; 99.59% used; 110407602 free inodes.

server2 `/mnt/raid5`: 321031172096 available bytes; 97.78% used; 445075346 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84272144384 available bytes; 95.30% used; 114154468 free inodes.

server3 `/home`: 84272144384 available bytes; 95.30% used; 114154468 free inodes.

server3 `/data`: 142208090112 available bytes; 98.03% used; 225808733 free inodes.

server3 `/tmp`: 84272144384 available bytes; 95.30% used; 114154468 free inodes.

server3 `/var/tmp`: 84272144384 available bytes; 95.30% used; 114154468 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654403072 available bytes; 94.10% used; 114349711 free inodes.

server4 `/home`: 105654403072 available bytes; 94.10% used; 114349711 free inodes.

server4 `/data`: 231441653760 available bytes; 96.80% used; 224946491 free inodes.

server4 `/tmp`: 105654403072 available bytes; 94.10% used; 114349711 free inodes.

server4 `/var/tmp`: 105654403072 available bytes; 94.10% used; 114349711 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
