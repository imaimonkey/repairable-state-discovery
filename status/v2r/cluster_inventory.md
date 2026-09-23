# V2R cluster inventory

2026-09-23T21:42:28.555710+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325712408576 available bytes; 81.83% used; 112501330 free inodes.

server1 `/home`: 325712408576 available bytes; 81.83% used; 112501330 free inodes.

server1 `/tmp`: 325712408576 available bytes; 81.83% used; 112501330 free inodes.

server1 `/var/tmp`: 325712408576 available bytes; 81.83% used; 112501330 free inodes.

server1 `/mnt/raid5`: 1388127899648 available bytes; 93.63% used; 337739923 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41115578368 available bytes; 97.71% used; 110432665 free inodes.

server2 `/home`: 41115578368 available bytes; 97.71% used; 110432665 free inodes.

server2 `/tmp`: 41115578368 available bytes; 97.71% used; 110432665 free inodes.

server2 `/var/tmp`: 41115578368 available bytes; 97.71% used; 110432665 free inodes.

server2 `/mnt/raid5`: 537601871872 available bytes; 96.29% used; 445208347 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292631912448 available bytes; 83.67% used; 114187274 free inodes.

server3 `/home`: 292631912448 available bytes; 83.67% used; 114187274 free inodes.

server3 `/data`: 52265660416 available bytes; 99.28% used; 225848546 free inodes.

server3 `/tmp`: 292631912448 available bytes; 83.67% used; 114187274 free inodes.

server3 `/var/tmp`: 292631912448 available bytes; 83.67% used; 114187274 free inodes.
| server4 | True | ['0', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106473136128 available bytes; 94.06% used; 114355972 free inodes.

server4 `/home`: 106473136128 available bytes; 94.06% used; 114355972 free inodes.

server4 `/data`: 300253872128 available bytes; 95.85% used; 225448459 free inodes.

server4 `/tmp`: 106473136128 available bytes; 94.06% used; 114355972 free inodes.

server4 `/var/tmp`: 106473136128 available bytes; 94.06% used; 114355972 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
