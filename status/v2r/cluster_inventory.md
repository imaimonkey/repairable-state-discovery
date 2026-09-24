# V2R cluster inventory

2026-09-24T00:38:10.749710+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325543964672 available bytes; 81.84% used; 112500503 free inodes.

server1 `/home`: 325543964672 available bytes; 81.84% used; 112500503 free inodes.

server1 `/tmp`: 325543964672 available bytes; 81.84% used; 112500503 free inodes.

server1 `/var/tmp`: 325543964672 available bytes; 81.84% used; 112500503 free inodes.

server1 `/mnt/raid5`: 1110133542912 available bytes; 94.91% used; 337735045 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40992698368 available bytes; 97.71% used; 110432312 free inodes.

server2 `/home`: 40992698368 available bytes; 97.71% used; 110432312 free inodes.

server2 `/tmp`: 40992698368 available bytes; 97.71% used; 110432312 free inodes.

server2 `/var/tmp`: 40992698368 available bytes; 97.71% used; 110432312 free inodes.

server2 `/mnt/raid5`: 532526436352 available bytes; 96.32% used; 445203077 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292341751808 available bytes; 83.69% used; 114196153 free inodes.

server3 `/home`: 292341751808 available bytes; 83.69% used; 114196153 free inodes.

server3 `/data`: 82235641856 available bytes; 98.86% used; 225844083 free inodes.

server3 `/tmp`: 292341751808 available bytes; 83.69% used; 114196153 free inodes.

server3 `/var/tmp`: 292341751808 available bytes; 83.69% used; 114196153 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106066165760 available bytes; 94.08% used; 114350130 free inodes.

server4 `/home`: 106066165760 available bytes; 94.08% used; 114350130 free inodes.

server4 `/data`: 292919853056 available bytes; 95.95% used; 225414580 free inodes.

server4 `/tmp`: 106066165760 available bytes; 94.08% used; 114350130 free inodes.

server4 `/var/tmp`: 106066165760 available bytes; 94.08% used; 114350130 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
