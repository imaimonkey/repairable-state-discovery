# V2R cluster inventory

2026-09-24T00:44:21.227503+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325539291136 available bytes; 81.84% used; 112500441 free inodes.

server1 `/home`: 325539291136 available bytes; 81.84% used; 112500441 free inodes.

server1 `/tmp`: 325539291136 available bytes; 81.84% used; 112500441 free inodes.

server1 `/var/tmp`: 325539291136 available bytes; 81.84% used; 112500441 free inodes.

server1 `/mnt/raid5`: 1083977572352 available bytes; 95.03% used; 337735001 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40982634496 available bytes; 97.71% used; 110432284 free inodes.

server2 `/home`: 40982634496 available bytes; 97.71% used; 110432284 free inodes.

server2 `/tmp`: 40982634496 available bytes; 97.71% used; 110432284 free inodes.

server2 `/var/tmp`: 40982634496 available bytes; 97.71% used; 110432284 free inodes.

server2 `/mnt/raid5`: 531790004224 available bytes; 96.33% used; 445202695 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292197220352 available bytes; 83.69% used; 114184626 free inodes.

server3 `/home`: 292197220352 available bytes; 83.69% used; 114184626 free inodes.

server3 `/data`: 82219220992 available bytes; 98.86% used; 225843603 free inodes.

server3 `/tmp`: 292197220352 available bytes; 83.69% used; 114184626 free inodes.

server3 `/var/tmp`: 292197220352 available bytes; 83.69% used; 114184626 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106055802880 available bytes; 94.08% used; 114349970 free inodes.

server4 `/home`: 106055802880 available bytes; 94.08% used; 114349970 free inodes.

server4 `/data`: 292915310592 available bytes; 95.95% used; 225414576 free inodes.

server4 `/tmp`: 106055802880 available bytes; 94.08% used; 114349970 free inodes.

server4 `/var/tmp`: 106055802880 available bytes; 94.08% used; 114349970 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
