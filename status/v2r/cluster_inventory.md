# V2R cluster inventory

2026-09-24T09:02:56.238402+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324374335488 available bytes; 81.90% used; 112490124 free inodes.

server1 `/home`: 324374335488 available bytes; 81.90% used; 112490124 free inodes.

server1 `/tmp`: 324374335488 available bytes; 81.90% used; 112490124 free inodes.

server1 `/var/tmp`: 324374335488 available bytes; 81.90% used; 112490124 free inodes.

server1 `/mnt/raid5`: 483094994944 available bytes; 97.78% used; 337716616 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57787412480 available bytes; 96.78% used; 110430967 free inodes.

server2 `/home`: 57787412480 available bytes; 96.78% used; 110430967 free inodes.

server2 `/tmp`: 57787412480 available bytes; 96.78% used; 110430967 free inodes.

server2 `/var/tmp`: 57787412480 available bytes; 96.78% used; 110430967 free inodes.

server2 `/mnt/raid5`: 515435708416 available bytes; 96.44% used; 445178634 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85892009984 available bytes; 95.21% used; 114199209 free inodes.

server3 `/home`: 85892009984 available bytes; 95.21% used; 114199209 free inodes.

server3 `/data`: 167051915264 available bytes; 97.69% used; 225821818 free inodes.

server3 `/tmp`: 85892009984 available bytes; 95.21% used; 114199209 free inodes.

server3 `/var/tmp`: 85892009984 available bytes; 95.21% used; 114199209 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759236096 available bytes; 94.10% used; 114349077 free inodes.

server4 `/home`: 105759236096 available bytes; 94.10% used; 114349077 free inodes.

server4 `/data`: 319632515072 available bytes; 95.58% used; 225273397 free inodes.

server4 `/tmp`: 105759236096 available bytes; 94.10% used; 114349077 free inodes.

server4 `/var/tmp`: 105759236096 available bytes; 94.10% used; 114349077 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
