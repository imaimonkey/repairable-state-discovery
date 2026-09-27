# V2R cluster inventory

2026-09-27T04:57:13.766841+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314801987584 available bytes; 82.44% used; 112443004 free inodes.

server1 `/home`: 314801987584 available bytes; 82.44% used; 112443004 free inodes.

server1 `/tmp`: 314801987584 available bytes; 82.44% used; 112443004 free inodes.

server1 `/var/tmp`: 314801987584 available bytes; 82.44% used; 112443004 free inodes.

server1 `/mnt/raid5`: 636044890112 available bytes; 97.08% used; 337400295 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17619644416 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17619644416 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17619644416 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17619644416 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 576047853568 available bytes; 96.02% used; 444878486 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78609756160 available bytes; 95.61% used; 114062917 free inodes.

server3 `/home`: 78609756160 available bytes; 95.61% used; 114062917 free inodes.

server3 `/data`: 1333654298624 available bytes; 81.57% used; 225758393 free inodes.

server3 `/tmp`: 78609756160 available bytes; 95.61% used; 114062917 free inodes.

server3 `/var/tmp`: 78609756160 available bytes; 95.61% used; 114062917 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111000604672 available bytes; 93.81% used; 114372922 free inodes.

server4 `/home`: 111000604672 available bytes; 93.81% used; 114372922 free inodes.

server4 `/data`: 382102740992 available bytes; 94.72% used; 224780466 free inodes.

server4 `/tmp`: 111000604672 available bytes; 93.81% used; 114372922 free inodes.

server4 `/var/tmp`: 111000604672 available bytes; 93.81% used; 114372922 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
