# V2R cluster inventory

2026-09-24T09:01:15.904993+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324375932928 available bytes; 81.90% used; 112490140 free inodes.

server1 `/home`: 324375932928 available bytes; 81.90% used; 112490140 free inodes.

server1 `/tmp`: 324375932928 available bytes; 81.90% used; 112490140 free inodes.

server1 `/var/tmp`: 324375932928 available bytes; 81.90% used; 112490140 free inodes.

server1 `/mnt/raid5`: 503742681088 available bytes; 97.69% used; 337716807 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57788473344 available bytes; 96.78% used; 110430971 free inodes.

server2 `/home`: 57788473344 available bytes; 96.78% used; 110430971 free inodes.

server2 `/tmp`: 57788473344 available bytes; 96.78% used; 110430971 free inodes.

server2 `/var/tmp`: 57788473344 available bytes; 96.78% used; 110430971 free inodes.

server2 `/mnt/raid5`: 515495116800 available bytes; 96.44% used; 445178793 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85899767808 available bytes; 95.21% used; 114199587 free inodes.

server3 `/home`: 85899767808 available bytes; 95.21% used; 114199587 free inodes.

server3 `/data`: 167063707648 available bytes; 97.69% used; 225821859 free inodes.

server3 `/tmp`: 85899767808 available bytes; 95.21% used; 114199587 free inodes.

server3 `/var/tmp`: 85899767808 available bytes; 95.21% used; 114199587 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759285248 available bytes; 94.10% used; 114349077 free inodes.

server4 `/home`: 105759285248 available bytes; 94.10% used; 114349077 free inodes.

server4 `/data`: 319642488832 available bytes; 95.58% used; 225273402 free inodes.

server4 `/tmp`: 105759285248 available bytes; 94.10% used; 114349077 free inodes.

server4 `/var/tmp`: 105759285248 available bytes; 94.10% used; 114349077 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
