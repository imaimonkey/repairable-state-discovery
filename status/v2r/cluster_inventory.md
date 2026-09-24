# V2R cluster inventory

2026-09-24T08:33:14.759902+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324402294784 available bytes; 81.90% used; 112490434 free inodes.

server1 `/home`: 324402294784 available bytes; 81.90% used; 112490434 free inodes.

server1 `/tmp`: 324402294784 available bytes; 81.90% used; 112490434 free inodes.

server1 `/var/tmp`: 324402294784 available bytes; 81.90% used; 112490434 free inodes.

server1 `/mnt/raid5`: 509281611776 available bytes; 97.66% used; 337720282 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57807912960 available bytes; 96.78% used; 110430997 free inodes.

server2 `/home`: 57807912960 available bytes; 96.78% used; 110430997 free inodes.

server2 `/tmp`: 57807912960 available bytes; 96.78% used; 110430997 free inodes.

server2 `/var/tmp`: 57807912960 available bytes; 96.78% used; 110430997 free inodes.

server2 `/mnt/raid5`: 516048433152 available bytes; 96.43% used; 445179523 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85482254336 available bytes; 95.23% used; 114174914 free inodes.

server3 `/home`: 85482254336 available bytes; 95.23% used; 114174914 free inodes.

server3 `/data`: 175041015808 available bytes; 97.58% used; 225822888 free inodes.

server3 `/tmp`: 85482254336 available bytes; 95.23% used; 114174914 free inodes.

server3 `/var/tmp`: 85482254336 available bytes; 95.23% used; 114174914 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105769156608 available bytes; 94.10% used; 114349116 free inodes.

server4 `/home`: 105769156608 available bytes; 94.10% used; 114349116 free inodes.

server4 `/data`: 257094959104 available bytes; 96.45% used; 225288401 free inodes.

server4 `/tmp`: 105769156608 available bytes; 94.10% used; 114349116 free inodes.

server4 `/var/tmp`: 105769156608 available bytes; 94.10% used; 114349116 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
