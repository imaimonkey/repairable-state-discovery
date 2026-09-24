# V2R cluster inventory

2026-09-24T06:38:13.092427+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324500930560 available bytes; 81.90% used; 112491594 free inodes.

server1 `/home`: 324500930560 available bytes; 81.90% used; 112491594 free inodes.

server1 `/tmp`: 324500930560 available bytes; 81.90% used; 112491594 free inodes.

server1 `/var/tmp`: 324500930560 available bytes; 81.90% used; 112491594 free inodes.

server1 `/mnt/raid5`: 517571977216 available bytes; 97.63% used; 337723748 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57875591168 available bytes; 96.77% used; 110431197 free inodes.

server2 `/home`: 57875591168 available bytes; 96.77% used; 110431197 free inodes.

server2 `/tmp`: 57875591168 available bytes; 96.77% used; 110431197 free inodes.

server2 `/var/tmp`: 57875591168 available bytes; 96.77% used; 110431197 free inodes.

server2 `/mnt/raid5`: 520004313088 available bytes; 96.41% used; 445191943 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126914531328 available bytes; 92.92% used; 114195218 free inodes.

server3 `/home`: 126914531328 available bytes; 92.92% used; 114195218 free inodes.

server3 `/data`: 139407228928 available bytes; 98.07% used; 225835564 free inodes.

server3 `/tmp`: 126914531328 available bytes; 92.92% used; 114195218 free inodes.

server3 `/var/tmp`: 126914531328 available bytes; 92.92% used; 114195218 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105805012992 available bytes; 94.10% used; 114349251 free inodes.

server4 `/home`: 105805012992 available bytes; 94.10% used; 114349251 free inodes.

server4 `/data`: 320575746048 available bytes; 95.57% used; 225372427 free inodes.

server4 `/tmp`: 105805012992 available bytes; 94.10% used; 114349251 free inodes.

server4 `/var/tmp`: 105805012992 available bytes; 94.10% used; 114349251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
